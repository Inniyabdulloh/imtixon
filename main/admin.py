from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'phone')
    search_fields = ('first_name', 'last_name')
    list_filter = ('first_name','last_name','age')


@admin.register(models.StaffPosition)
class StaffPositionAdmin(admin.ModelAdmin):
    list_display = ('staff', 'position')
    search_fields = ('staff','position')
    list_filter = ('position',)


@admin.register(models.StaffShift)
class StaffShiftAdmin(admin.ModelAdmin):
    list_display = ('staff','shift')
    search_fields = ('staff','shift')
    list_filter = ('shift',)


@admin.register(models.StaffAttandance)
class StaffAttandanceAdmin(admin.ModelAdmin):
    list_display = ('staff','check_in', 'check_out')
    search_fields = ('staff',)
    list_filter = ('staff',)


admin.site.register(models.Position)
admin.site.register(models.Shift)