from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post, Comment

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_picture')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'author')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = User.objects.all()

#Comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter your comment here...'}),
        }

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) < 10:
            raise forms.ValidationError("Comment must be at least 10 characters long.")
        return content