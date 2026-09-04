from django.shortcuts import render, get_object_or_404
from .models import Spirit

def spirit_list(request):
    spirits = Spirit.objects.all()
    return render(request, 'spirits/spirit_list.html', {'spirits': spirits})

def spirit_detail(request, pk):
    spirit = get_object_or_404(Spirit, pk=pk)
    return render(request, 'spirits/spirit_detail.html', {'spirit': spirit})