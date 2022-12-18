from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'category', 'image', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-field-test'}),
            'pub_date': forms.DateInput(format=('%m/%d/%Y'), 
            attrs={'class':'form-control', 
            'placeholder':'Select a date',
            'type':'date'}),
            'category': forms.Select(attrs={'class': 'form-field-test'}),
            'image': forms.URLInput(attrs={'class': 'form-field-test'}),
            }