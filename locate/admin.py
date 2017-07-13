from django.contrib import admin
from .models import locate

class LocateAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude')

admin.site.register(locate, LocateAdmin)