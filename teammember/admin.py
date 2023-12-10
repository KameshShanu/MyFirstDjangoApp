from django.contrib import admin
from .models import Teammember

# Register your models here.
@admin.register(Teammember)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }