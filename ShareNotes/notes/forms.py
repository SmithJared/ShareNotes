from django import forms
from notes.models import Classroom, NoteCreate

class ClassroomSelectForm(forms.Form):
    classroom = forms.ModelChoiceField(queryset=Classroom.objects.all())

class NoteUploadForm(forms.ModelForm):
    class Meta:
        model = NoteCreate
        fields = ['image', 'caption']