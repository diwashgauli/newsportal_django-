from django import forms
from newspaper.models import Post
from django.contrib.admin.widgets import AdminSplitDateTime

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['featured_image', 'title', 'category', 'tag']

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'featured_image', 'category', 'tag']
