from django.contrib import admin
from .models import Post


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('text', 'publish_datetime', 'owner')
    autocomplete_fields = ('owner', )

# Register your models here.
