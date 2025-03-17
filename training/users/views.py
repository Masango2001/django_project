from django.shortcuts import render,redirect,get_object_or_404
from.models import student
from.forms import studentForm
def home(request):
    return render(request,'index.html')
def nos_services(request):
    return render(request,'nos_services.html')
def create_student(request):
    if request.method=='POST':
        form=studentForm(request.POST)
        if forms.is_valid():
            form.save()
            return redirect('home')
        else:
            form=studentForm()
            return render(request,'form.html',{'form':form})
def edit_student(request,id):
    student=get_object_or_404(Student,id=id)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form=StudentForm(request.POST,instance=student)
            return render(request,'form.html',{'form':form})
def delete_student(request,id):
    Student=get_object_or_404(Students,id=id)
    if request.method=='POST':
        students.Delete()
        return redirect('home')
    return render(request,'service.html',{'student':student})        
