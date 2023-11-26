from django.contrib import admin

from chat.models import *


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('message', 'send_at')

