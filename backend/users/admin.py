from django.contrib import admin
from .models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('role', 'is_staff')

admin.site.register(User, UserAdmin)