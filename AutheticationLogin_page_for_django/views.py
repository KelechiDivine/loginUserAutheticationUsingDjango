from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import


# Create your views here.

def indexView(request):
    return render(request, 'registration/base.html')

@login_required
def dashboardView(request):
    return render(request, 'registration/dashboard.html ')

def registerView(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('login_url')
    
    else:
        form  = UserCreationForm()
    return render(request, 'registration/register.html',
                  {
                      'form': form
                  })
        
    return render(request, 'registration/register.html')