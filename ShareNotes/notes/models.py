from django.db import models
from django.contrib.auth.models import Permission
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Classroom(models.Model):
    classroom_name = models.CharField(max_length=30)
    students = models.ManyToManyField(settings.AUTH_USER_MODEL)
    
    def __str__(self):
        return self.classroom_name
    
class UploadedFile(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, blank=True,null=True )
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    name = models.TextField(default="name")
    note = models.TextField()
    file = models.FileField(upload_to='documents/') # for creating file input  
    upload_date = models.DateTimeField(auto_now_add=True)

def assign_permission_to_student(classroom_id, student):
    permission = Permission.objects.get(codename='view_classroom_files')
    classroom = Classroom.objects.get(id=classroom_id)
    classroom.user.add(settings.AUTH_USER_MODEL)
    student.user.user_permissions.add(permission)

class Note(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_notes')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_notes')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
