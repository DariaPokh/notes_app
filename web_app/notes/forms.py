from .models import Note
from django.forms import ModelForm, TextInput, FileInput, Textarea


class NoteForm(ModelForm):
    """Создание формы для отображения модели Note"""
    class Meta:
        model = Note
        fields = ['title', 'text', 'img']
        widgets = {
            'title': TextInput(attrs={
               'class': 'form-control',
               'placeholder': 'Название'}),

            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст заметки'}),

            'img': FileInput(attrs={
                'class': 'form-control'})}
