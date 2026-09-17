from django import forms
from .models import Review, Spirit

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'spirit_image', 'text', 'date_tried', 'location']
        widgets = {
            'rating': forms.HiddenInput(),
            'spirit_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'date_tried': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'location': forms.HiddenInput(),
        }

class SpiritForm(forms.ModelForm):
    class Meta:
        model = Spirit
        fields = ['name', 'category', 'brand', 'abv', 'description', 'spirit_default_image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'abv': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'spirit_default_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }