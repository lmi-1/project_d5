from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'postCategory',
            'text',
        ]
    def clean_title(self):
        title_posts = self.cleaned_data["title"]
        if title_posts[0].islower():
            raise ValidationError(
                "Заголовок должен начинаться с заглавной буквы"
            )
        return title_posts

    def clean_text(self):
        text_posts = self.cleaned_data["text"]
        if text_posts[0].islower():
            raise ValidationError(
                "Текст должен начинаться с заглавной буквы"
            )
        return text_posts
