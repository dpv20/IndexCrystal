from django.contrib import admin
from .models import ExternalWebpageUser
from .models import Employee

class ExternalWebpageUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'webpage_url', 'external_username')
    search_fields = ('user__username', 'webpage_url')

admin.site.register(ExternalWebpageUser, ExternalWebpageUserAdmin)




@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'department', 'country', 'email', 'company')
