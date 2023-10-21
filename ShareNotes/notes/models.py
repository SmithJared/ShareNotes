from django.db import models
from django import forms  
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User


# Create your models here.

class StudentForm(models.Model):  
    # firstname = forms.CharField(label="Enter first name",max_length=50)  
    # lastname  = forms.CharField(label="Enter last name", max_length = 10)    
    file = models.FileField(upload_to='documents/') # for creating file input  


class Classroom(models.Model):
    classroom_name = models.CharField(max_length=30)
    students = models.ManyToManyField(User)
    
    def __str__(self):
        return self.classroom_name

class note(models.Model):
    title = models.CharField(max_length=100)
    note_date = models.DateField()
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Meta:
    ordering = ["title"]
    
class UploadedFile(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    note = models.ForeignKey(note, on_delete=models.CASCADE)
    file = models.FileField(upload_to='upload/')  # Define the upload path
    upload_date = models.DateTimeField(auto_now_add=True)

def assign_permission_to_student(classroom_id, student):
    permission = Permission.objects.get(codename='view_classroom_files')
    classroom = Classroom.objects.get(id=classroom_id)
    classroom.user.add(User)
    student.user.user_permissions.add(permission)