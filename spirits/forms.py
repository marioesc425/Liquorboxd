from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'spirit_image', 'text', 'date_tried']
        widgets = {
            'rating': forms.HiddenInput(),
            'spirit_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'date_tried': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }