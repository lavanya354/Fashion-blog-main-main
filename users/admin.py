from django.contrib import admin

# Register your models here.

from .models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['image_type', 'description', 'image_file']
