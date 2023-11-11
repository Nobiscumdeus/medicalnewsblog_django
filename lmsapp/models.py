from django.db import models
from accounts.models import CustomUser
from ckeditor.fields import RichTextField


#We need to create our user groups in order to create their roles 
from django.contrib.auth.models import Group

#Lets create a group for our instructors 
instructor_group,created=Group.objects.get_or_create(name='Instructors')
#Create a group for students 
student_group,created=Group.objects.get_or_create(name="Students")
#Create a group for Administrators 
admin_group,created=Group.objects.get_or_create(name='Administrators')

#Adding some users to the groups available
#Get the user and the group
user=CustomUser.objects.get(username='Chasfat')
group=Group.objects.get(name='Instructors')
#Assign the user to the group
user.groups.add(group)

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    instructor = models.ForeignKey('InstructorProfile',blank=True,null=True, on_delete=models.CASCADE)
    objectives = RichTextField()
    prerequisites = RichTextField()
    syllabus = RichTextField()
    start_date = models.DateField()
    end_date = models.DateField()
    enrollment_limit = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_published = models.BooleanField(default=False)
    students_enrolled = models.ManyToManyField('StudentProfile', related_name='courses_enrolled',blank=True,null=True)
    students_completed = models.ManyToManyField('StudentProfile', related_name='courses_completed',blank=True,null=True)

    def __str__(self):
        return self.title

class StudentProfile(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    date_of_birth=models.DateField()
    medical_school=models.CharField(max_length=100)
    completed_courses=models.ManyToManyField('Course',related_name='students_completed_courses',blank=True,null=True)
    enrolled_courses=models.ManyToManyField('Course',related_name='students_enrolled_courses',blank=True,null=True)
    degree_program=models.CharField(max_length=15,null=True,blank=True)
    def __str__(self):
        return f"{self.user}"
    
class StudentProgress(models.Model):
    student=models.ForeignKey(StudentProfile,on_delete=models.CASCADE)
    courses=models.ManyToManyField('Course',related_name='student_courses',blank=True,null=True)
    completed_modules=models.ManyToManyField('Course',related_name='student_completed_modules',blank=True,null=True)
    current_module=models.ForeignKey(Course,null=True,blank=True,on_delete=models.CASCADE)
    grade=models.FloatField(null=True,blank=True)
    def __str__(self):
        return f"{self.current_module}"
    
    
class InstructorProfile(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    medical_degree=models.CharField(max_length=100)
    specialization=RichTextField()
    courses_taught=models.ManyToManyField('Course',related_name='instructor_courses_taught',blank=True,null=True)
    def __str__(self):
        return f"{self.user}"
    
class AdministratorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    responsibilities = RichTextField()
    def __str__(self):
        return f"{self.user}"
    