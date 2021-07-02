from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    '''
    Makes the form smaller, removes the
    label and add a placeholder to the field
    '''
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say something...'
        }))

    image = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['body', 'image']


class CommentForm(forms.ModelForm):
    '''
    Makes the form smaller, removes the
    label and add a placeholder to the field
    '''
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say something...'
        }))

    class Meta:
        model = Comment
        fields = ['comment']
