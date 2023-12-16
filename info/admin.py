from django.contrib import admin
from info.models import *


# Register your models here.



class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class DayAdmin(admin.ModelAdmin):
    list_display = ('day',)
    search_fields = ('day',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','password')



admin.site.register(Department, DepartmentAdmin)
admin.site.register(Day, DayAdmin)
admin.site.register(CustomUser, UserAdmin)

