
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from accounts.forms import ProfileForm
from accounts.models import Profile
from spirits.models import Review


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            # Create a Profile for the new user
            Profile.objects.create(user=user)

            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile(request):
    reviews = Review.objects.filter(user=request.user)

    # Get the user's profile
    profile = request.user.profile

    possible_ratings = [
        0, 0.5, 1, 1.5, 2, 2.5,
        3, 3.5, 4, 4.5, 5
    ]

    distribution = []

    for rating in possible_ratings:
        count = reviews.filter(rating=rating).count()

        distribution.append({
            'rating': rating,
            'count': count
        })

    max_count = (
        max([d['count'] for d in distribution])
        if any(d['count'] for d in distribution)
        else 1
    )

    return render(request, 'accounts/profile.html', {
        'reviews': reviews,
        'profile': profile,
        'distribution': distribution,
        'max_count': max_count,
    })


@login_required
def add_avatar(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'accounts/add_avatar.html', {
        'form': form
    })
