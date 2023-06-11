from django.contrib import admin
from . import models
# Register your models here.


class CourseItemInline(admin.TabularInline):
    model = models.CourseItem
    raw_id_fields = ['student']



admin.site.register(models.Faculty)
admin.site.register(models.Department)
admin.site.register(models.Semester)
admin.site.register(models.Student)


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'course_code']

    inlines = [CourseItemInline]





