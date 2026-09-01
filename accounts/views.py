from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        ##UserCreationForm(request.POST) — when there's submitted data, you pass it into the form so Django can validate it against that data. UserCreationForm() with nothing passed in (the else branch) just gives you an empty, unbound form to display.
        form = UserCreationForm(request.POST)
        ##Django built in validation — checks that the username is unique, the password meets requirements, and the two password fields match. If any of those fail, form.is_valid() returns False and the form will be re-rendered with error messages.
        if form.is_valid():
            form.save()
            ##sends the browser to a URL named 'login'
            return redirect('login')
    else:
        form = UserCreationForm()
    ##Template rendering — the form is passed into the template context so it can be displayed to the user. If there were validation errors, those will also be included in the form object and displayed in the template.
    return render(request, 'accounts/register.html', {'form': form})
