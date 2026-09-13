from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'text', 'date_tried']
        widgets = {
            'rating': forms.HiddenInput(),
        }