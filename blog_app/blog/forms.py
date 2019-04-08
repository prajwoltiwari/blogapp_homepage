from django import forms 

from .models import Comment, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        exclude = ['date_posted', 'author']

class CommentForm(forms.ModelForm):
    comment = forms.CharField(required = False, widget=forms.TextInput(attrs={'placeholder': 'Type in your comment', 'cols':74.5, 'rows':3}))
    class Meta:
        model = Comment
        exclude = ('admitted','date_posted', 'author', 'post')


       