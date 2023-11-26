from urllib.parse import urlencode

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from chat.forms import RegisterUserForm, AuthUserForm
from chat.models import Message, User, Room


class ChatView(View):
    def get(self, request, room_id):
        messages = Message.objects.filter(room_id=room_id)
        print(request.GET.get('user_id'))
        user = User.objects.get(pk=request.GET.get('user_id'))
        rooms = Room.objects.all()
        return render(request, 'chat/chat.html',
                      context={'messages': messages, 'user': user, 'rooms': rooms, 'room_active': room_id})


class AuthView(View):
    def get(self, request):
        form = AuthUserForm()
        return render(request, 'chat/auth.html', context={'form': form})

    def post(self, request):
        form = AuthUserForm(request.POST)
        user = User.objects.get(email=request.POST.get('email'))
        if user:
            if user.password == request.POST.get('password'):
                params = urlencode({'user_id': user.id})
                return redirect(to=reverse_lazy('chat:chat', args=[1]) + '?' + params)
        return render(request, 'chat/auth.html', context={'error': 'Wrong email or password', 'form': form})


class RegisterView(CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'chat/register.html'
    success_url = reverse_lazy('chat:auth')

    def form_valid(self, form):
        user = form.save(commit=False)
        print(form.cleaned_data.get("password"))
        user.set_password(form.cleaned_data.get("password"))
        user.save()
        return super().form_valid(form=form)
