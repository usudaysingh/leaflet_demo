from django.contrib import admin
from .models import locate, AppUser

class LocateAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude')

class UserAdmin(admin.ModelAdmin):
	list_display = ('username',)

admin.site.register(AppUser, UserAdmin)
admin.site.register(locate, LocateAdmin)