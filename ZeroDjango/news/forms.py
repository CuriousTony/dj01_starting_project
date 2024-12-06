from .models import Article
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'intro', 'content', 'author', 'date']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок'}),
            'intro': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание'}),
            'content': Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст статьи'}),
            'author': TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор'}),
            'date': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})
        }
