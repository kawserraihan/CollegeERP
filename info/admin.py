from django.contrib import admin
from info.models import *

# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_name','department','email','contact_number', 'user', 'address', 'status')
    search_fields = ('teacher_name',)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class BusDayAdmin(admin.ModelAdmin):
    list_display = ('day',)
    search_fields = ('day',)




admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(BusDay, BusDayAdmin)

