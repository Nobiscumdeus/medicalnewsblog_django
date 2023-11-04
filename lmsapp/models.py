from django.db import models
from django.contrib.auth.models import CustomUser
User=CustomUser()

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey('InstructorProfile', on_delete=models.CASCADE)
    objectives = models.TextField()
    prerequisites = models.TextField()
    syllabus = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    enrollment_limit = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_published = models.BooleanField(default=False)
    students_enrolled = models.ManyToManyField('StudentProfile', related_name='enrolled_courses')
    students_completed = models.ManyToManyField('StudentProfile', related_name='completed_courses')

    def __str__(self):
        return self.title

class StudentProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    date_of_birth=models.DateField()
    medical_school=models.CharField(max_length=100)
    completed_courses=models.ManyToManyField('Course',related_name='student_completed')
    enrolled_courses=models.ManyToManyField('Course',related_name='students_enrolled')
    
class StudentProgress(models.Model):
    student=models.ForeignKey(StudentProfile,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    completed_modules=models.ManyToManyField('Module')
    current_module=models.ForeignKey('Module',null=True,blank=True,on_delete=models.CasCADE)
    grade=models.FloatField(null=True,blank=True)
    
    
class InstructorProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    medical_degree=models.CharField(max_length=100)
    specialization=models.Textfield()
    courses_taught=models.ManyToManyField('Course')
    
class AdministratorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    responsibilities = models.TextField()