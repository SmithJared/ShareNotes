from django.db import models
from django import forms  

# Create your models here.
class StudentForm(forms.Form):  
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length = 10)    
    file      = forms.FileField() # for creating file input  