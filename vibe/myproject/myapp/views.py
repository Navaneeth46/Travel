from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def package1(request):
    return render(request,'package1.html')
def package2(request):
    return render(request,'package2.html')
def contacts(request):
    return render(request,'contacts.html')


