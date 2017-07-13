from django.contrib import admin
from .models import locate, around_locations

class LocateAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude')

class AroundLocationsAdmin(admin.ModelAdmin):
	list_display = ('name', 'latitude', 'longitude')

admin.site.register(locate, LocateAdmin)
admin.site.register(around_locations, AroundLocationsAdmin)