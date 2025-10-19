from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')


def p1(request):
    return render(request, 'project1.html')


def p2(request):
    return render(request, 'project2.html')


def p3(request):
    return render(request, 'project3.html')
