from django import forms

from chat.models import User


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(
                attrs={'type': 'text', 'name': 'name', 'class': 'form-control', 'id': 'floatingInput',
                       'placeholder': 'Name'}),
            'email': forms.EmailInput(
                attrs={'type': 'email', 'name': 'email', 'class': 'form-control', 'id': 'floatingInput',
                       'placeholder': 'Email'}),
            'password': forms.PasswordInput(
                attrs={'type': 'password', 'name': 'password', 'class': 'form-control', 'id': 'floatingPassword',
                       'placeholder': 'Password'})
        }


class AuthUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')
        widgets = {
            'email': forms.EmailInput(
                attrs={'type': 'email', 'name': 'email', 'class': 'form-control', 'id': 'floatingInput',
                       'placeholder': 'name@example.com'}),
            'password': forms.PasswordInput(
                attrs={'type': 'password', 'name': 'password', 'class': 'form-control', 'id': 'floatingPassword',
                       'placeholder': 'Password'})}
