from django.shortcuts import render
from .models import Spirit
# Create your views here.
def spirit_list(request):
    spirits = Spirit.objects.all()
    return render(request, 'spirits/spirit_list.html', {'spirits': spirits})