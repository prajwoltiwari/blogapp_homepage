from django import forms 
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import ReviewRating, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        exclude = ['date_posted', 'author']

class ReviewRatingForm(forms.ModelForm):
    review = forms.CharField(required = False, widget=forms.TextInput(attrs={'placeholder': 'Type in your comment', 'cols':74.5, 'rows':3}))
    rating = forms.IntegerField(required = True, validators=[MinValueValidator(1), MaxValueValidator(10)])
    class Meta:
        model = ReviewRating
        exclude = ('admitted','date_posted', 'author', 'post')



       