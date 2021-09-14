from django.contrib import admin
from .models import User


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', )
# Register your models here.
