from .models import Post
from django.forms import ModelForm, TextInput


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'title', 'body_post', 'image']

        widgets = {
            "user": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Користувач"
            }),
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Заголовок"
            }),
            "body_post": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Стаття"
            }),
            "image": TextInput(attrs={
                "type": "file",
                "name": "image",
                "accept": "image/*",
                "id": "id_image"
            })
        }
