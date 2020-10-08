from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Snippet	

# Register your models here.
@register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'language', 'owner', 'borrado')
    search_fields = ('title',)