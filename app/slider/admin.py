from django.contrib import admin
from .models import Slider

@admin.register(Slider)
class slideradmin(admin.ModelAdmin):
    list_display = ['description','tagline','link']
    list_filter = ['description','tagline','link']