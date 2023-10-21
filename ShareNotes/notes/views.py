from django.shortcuts import render
from django.http import HttpResponse
from notes.functions import handle_uploaded_file  
from notes.models import StudentForm  

# Create your views here.
def index(request, first_name): 
    stu = student.objects.get(first_name=first_name) 
    if request.method == 'POST':  
        form = StudentForm(request.POST, request.FILES)  
        if form.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            uploaded_file = form.save(commit=False)
            uploaded_file.stu = stu
            uploaded_file.save()
            return HttpResponse("File uploaded successfuly")  
    else:  
        student = StudentForm()  
        return render(request,"index.html",{'form':form})  

