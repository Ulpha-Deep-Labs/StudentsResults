from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=200)
    departments = models.ManyToManyField('Department', related_name='departments')

class Department(models.Model):
    name = models.CharField(max_length=200)
    course_adviser = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    students = models.ManyToManyField('Student', related_name='students_in_dept')


class Student(models.Model):
    reg_no = models.IntegerField()
    profile = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    courses = models.ManyToManyField('Course', related_name='courses_offered')
    level = models.CharField(max_length=3)



class Semester(models.Model):
    name = models.CharField(max_length=50)
    session = models.CharField(max_length=20)

class Course(models.Model):
    name = models.CharField(max_length=200)
    course_code = models.CharField(max_length=20)
    lecturer =  models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    student_offering_course = models.ForeignKey(Student, related_name='students_offering_course', on_delete=models.CASCADE)
    student_course_ca = models.IntegerField()
    student_course_exam_score = models.IntegerField()
    student_grade = models.CharField(max_length=1, blank=True)


    def save(self, *args, **kwargs):
        if self.student_course_ca + self.student_course_exam_score >=70:
            self.student_grade = "A"
        elif self.student_course_ca + self.student_course_exam_score >=69:
            self.student_grade = "B"
        elif self.student_course_ca + self.student_course_exam_score >=59:
            self.student_grade ="C"

        else:
            self.grade = "D"
        super().save(*args, **kwargs)





