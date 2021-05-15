from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    '''
    Makes the form smaller, removes the label and add a placehplder to the field
    '''
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say something...'
        }))

    class Meta:
        model = Post
        fields = ['body']
