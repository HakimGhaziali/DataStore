from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationsForm , CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationsForm
    form =  CustomUserChangeForm
    list_display = ('email', 'username', )


admin.site.register(CustomUser , CustomUserAdmin)