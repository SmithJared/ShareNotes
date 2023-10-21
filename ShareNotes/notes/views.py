from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from notes.functions import handle_uploaded_file  
from notes.models import StudentForm  
from django.contrib.auth.decorators import permission_required
from notes.models import Classroom
from notes.models import UploadedFile


# Create your views here.
def index(request: HttpRequest): 
    if request.method == 'POST':  
        form = StudentForm()
        form.file = request.FILES.get("file_input")  
        if form.file != None:  
            form.save()
            #handle_uploaded_file(request.FILES['file_input'])  
            # uploaded_file = form.save(commit=False)
            # uploaded_file.User
            # uploaded_file.save()
            return HttpResponse("<h1>File uploaded successfuly</h1>")  
        print("Here I am")
    else:  
        student = StudentForm()  
        return render(request,"notes/index.html")  

@permission_required('your_app.view_classroom_files', (Classroom, 'id', 'classroom_id'))
def view_classroom_files(request, classroom_id):
    classroom = Classroom.objects.get(id=classroom_id)
    files = UploadedFile.objects.filter(classroom=classroom)
    return render(request, 'classroom_files.html', {'files': files})

