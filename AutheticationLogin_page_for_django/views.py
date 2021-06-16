from django.shortcuts import render

# Create your views here.

def indexView(request):
    return render(request, 'registration/base.html')

def dashboardView(request):
    return render(request, 'registration/dashboard.html ')

def registerView(request):
    return render(request, 'registration/register.html')
    # return render(request, 'register.html')