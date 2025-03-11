from django.shortcuts import render
def home(request):
    return render(request,'index.html')
def nos_services(request):
    return render(request,'nos_services.html')