from django import forms
from .models import Classroom, Note

class ClassroomSelectForm(forms.Form):
    classroom = forms.ModelChoiceField(queryset=Classroom.objects.all())

