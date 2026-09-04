from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    ##Meta class tells Django which model to use to create the form and which fields to include in the form.
    class Meta:
        ##Base off Review model
        model = Review
        ##Should appear in the form
        fields = ['rating', 'text', 'date_tried']