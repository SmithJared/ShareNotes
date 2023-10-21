from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import permission_required
from notes.models import Classroom
from notes.models import UploadedFile


# Create your views here.
def index(request: HttpRequest): 
    if request.method == 'POST':  
        form = UploadedFile()
        form.file = request.FILES.get("file_input")  
        if form.file != None:  
            form.save()
            return HttpResponse("<h1>File uploaded successfuly</h1>")  
        print("Here I am")
    else:  
        return render(request,"notes/index.html") 

def student(req: HttpRequest, last_name):
    return render(req,"notes/base.html",{'user':req.user}) 

@permission_required('your_app.view_classroom_files', (Classroom, 'id', 'classroom_id'))
def view_classroom_files(request, classroom_id):
    classroom = Classroom.objects.get(id=classroom_id)
    files = UploadedFile.objects.filter(classroom=classroom)
    return render(request, 'classroom_files.html', {'files': files})

