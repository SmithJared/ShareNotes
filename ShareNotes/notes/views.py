from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, FileResponse
from django.contrib.auth.decorators import permission_required
from notes.models import Classroom
from notes.models import UploadedFile
from django.shortcuts import render, redirect
from notes.models import Note
from django.contrib.auth.decorators import login_required
from notes.models import User
from notes.forms import ClassroomSelectForm

# Create your views here.
@login_required
def upload(req: HttpRequest): 
    if req.method == 'POST':  
        form = UploadedFile()
        form.file = req.FILES.get("file_input")  
        if form.file != None:  
            form.name = req.FILES.get("file_input").name
            form.save()
            return redirect("/splash/") 
        
        return render(req,"notes/upload_note.html") 
    else:  
        return render(req,"notes/upload_note.html") 
    
@login_required
def splash(req:HttpRequest):
    files = UploadedFile.objects.filter(student=req.user)
    return render(req, "notes/index.html", {"files": files})

def view_files(req:HttpRequest, name):
    path = str(settings.MEDIA_ROOT) + "/documents/" + name
    print(path)
    return render(req, "notes/view_file.html", {'path':path})

def student(req: HttpRequest, last_name):
    return render(req,"notes/base.html",{'user':req.user}) 

@permission_required('your_app.view_classroom_files', (Classroom, 'id', 'classroom_id'))
def view_classroom_files(request, classroom_id):
    classroom = Classroom.objects.get(id=classroom_id)
    files = UploadedFile.objects.filter(classroom=classroom)
    return render(request, 'classroom_files.html', {'files': files})

@login_required
def create_note(request, recipient_id):
    recipient = User.objects.get(id=recipient_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        Note.objects.create(sender=request.user, recipient=recipient, content=content)
        return redirect('inbox')  # Redirect to the inbox or another page
    return render(request, 'create_note.html', {'recipient': recipient})

@login_required
def inbox(request):
    received_notes = Note.objects.filter(recipient=request.user).order_by('-timestamp')
    return render(request, 'inbox.html', {'received_notes': received_notes})

@login_required
def select_classroom(request):
    if request.method == 'POST':
        form = ClassroomSelectForm(request.POST)
        if form.is_valid():
            classroom = form.cleaned_data['classroom']
            notes = Note.objects.filter(classroom=classroom)
            return render(request, 'classroom.html', {'classroom': classroom, 'notes': notes})
    else:
        form = ClassroomSelectForm()
    return render(request, 'select_classroom.html', {'form': form})

@login_required
def classroom(request):
    # Display all classrooms for the user
    classrooms = Classroom.objects.filter(users=request.user)
    return render(request, 'classroom_list.html', {'classrooms': classrooms})