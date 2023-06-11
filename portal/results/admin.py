from django.contrib import admin
from . import models
# Register your models here.


class CourseItemInline(admin.TabularInline):
    model = models.CourseItem
    raw_id_fields = ['student']

@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'course_code']

    inlines = [CourseItemInline]



admin.site.register(models.Faculty)
admin.site.register(models.Department)
admin.site.register(models.Session)
admin.site.register(models.Student)







