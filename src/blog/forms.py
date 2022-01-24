from django import form
from django import fforms
from django.forms import forms


class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Taxtarea)