from django.shortcuts import render

# Create your views here.

##Home view is the main page of the website, it will render the home.html template when accessed.
def home(request):
    return render(request, 'core/home.html')