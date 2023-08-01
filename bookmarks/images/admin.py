from .models import Image
from django.contrib import admin
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
 list_display = ['title', 'slug']
