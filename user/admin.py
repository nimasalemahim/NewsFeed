from django.contrib import admin
from .models import User, Subscription


class FollowerInline(admin.TabularInline):
    model = Subscription
    fk_name = "follower"
    autocomplete_fields = ("followed", )
    extra = 1


class FollowedInline(admin.TabularInline):
    model = Subscription
    fk_name = "followed"
    autocomplete_fields = ("follower", )
    extra = 1


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('username', 'email')
    inlines = (FollowerInline, FollowedInline)
    search_fields = ('username',)
    autocomplete_fields = ('followers',)
# Register your models here.
