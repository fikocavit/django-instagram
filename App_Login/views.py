from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def signup(request):
    form=UserCreationForm
    registered=False
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            registered=True
    return render(request, 'sign_up.html',context={
        'form': form,
        'registered':registered
    })
    
