from django import forms 

from .models import Comment

class CommentForm(forms.ModelForm):
    comment = forms.CharField(required = False, widget=forms.TextInput(attrs={'placeholder': 'Type in your comment', 'cols':74.5, 'rows':3}))
    class Meta:
        model = Comment
        exclude = ('admitted','date_posted', 'author', 'post')


       