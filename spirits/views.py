from django.shortcuts import render, redirect, get_object_or_404
from .models import Spirit
from .forms import ReviewForm, SpiritForm
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SpiritSerializer
from django.db.models import Avg
import random
from .models import Spirit, Review

def spirit_list(request):
    query = request.GET.get('q')    
    if query:
        spirits = Spirit.objects.filter(name__icontains=query)
    else:
        spirits = Spirit.objects.all()
    return render(request, 'spirits/spirit_list.html', {'spirits': spirits})

def spirit_detail(request, pk):
    spirit = get_object_or_404(Spirit, pk=pk)
    reviews = spirit.review_set.all()
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    return render(request, 'spirits/spirit_detail.html', {'spirit': spirit, 'reviews': reviews, 'average': avg_rating})

@login_required
def add_review(request, pk):
    ##pk=pk means that the primary key of the spirit is passed to the view function as an argument. This is used to retrieve the specific spirit from the database.
    ##get_object_or_404 is a Django shortcut that retrieves an object from the database based on the given model and primary key. If the object does not exist, it raises a 404 error.
    spirit = get_object_or_404(Spirit, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            ##Here this is establishing a relationship between the review and the user who submitted it, as well as the spirit that the review is about. The review is then saved to the database. This is presented in the spirit_detail view, which displays the details of a specific spirit along with its reviews.
            review = form.save(commit=False)
            review.user = request.user
            review.spirit = spirit
            review.save()
            return redirect('spirit_detail', pk=spirit.pk)
    else:
        ##Here ReviewForm() is called to create a new instance of the form. This instance is then passed to the template context, allowing the template to render the form fields for the user to fill out.
        form = ReviewForm()
    return render(request, 'spirits/add_review.html', {'form': form, 'spirit': spirit})

@api_view(['GET'])
def spirit_list_api(request):
    spirits = Spirit.objects.all()
    serializer = SpiritSerializer(spirits, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def spirit_detail_api(request, pk):
    spirit = get_object_or_404(Spirit, pk=pk)
    serializer = SpiritSerializer(spirit)
    return Response(serializer.data)

@login_required
def add_spirit(request):
    if request.method == 'POST':
        form = SpiritForm(request.POST, request.FILES)
        if form.is_valid():
            spirit = form.save()
            return redirect('spirit_detail', pk=spirit.pk)
    else:
        form = SpiritForm()
    return render(request, 'spirits/add_spirit.html', {'form': form})

@login_required
def edit_review(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            return redirect('spirit_detail', pk=review.spirit.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'spirits/edit_review.html', {'form': form, 'review': review})

@login_required
def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)
    spirit_pk = review.spirit.pk
    review.delete()
    return redirect('spirit_detail', pk=spirit_pk)

def drink_wheel(request):
    spirits = Spirit.objects.all()
    return render(request, 'spirits/drink_wheel.html', {'spirits': spirits})