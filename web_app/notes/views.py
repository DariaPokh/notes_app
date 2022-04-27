from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView

from .models import Note
from .forms import NoteForm


def home(request):
    """Выводит на главную страницу веб-сервиса все данные из модели Note.
    Отображение всех имеющихся заметок"""
    notes = Note.objects.order_by('-created')
    return render(request, 'home.html', {'notes': notes})


class NoteDetailView(DetailView):
    """Представление модели Note в виде списка"""
    model = Note
    template_name = 'detail_view.html'
    context_object_name = 'note'


class NoteUpdateView(UpdateView):
    """Представление для обновления данных в модели Note"""
    model = Note
    template_name = 'create.html'
    form_class = NoteForm


class NoteDeleteView(DeleteView):
    """Представление для удаление данных из модели Note"""
    model = Note  # Используемая в классе модель
    success_url = '/'  # ссылка страницы, на которую переходит пользователь после удаления информации
    template_name = 'note_delete.html'  # html-шаблон страницы для удаления заметки


def create(request):
    """Метод для создания новой записи в базе данных"""
    error = ''
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():  # Если запрос является post-запросом, то переданные данные проверяются на
            # соответствие требованиям к полям модели. В случае соответствия переданные данные добавляются в базу
            # данных, а пользователь возвращается на главную страницу
            form.save()
            return redirect('home')
        else:   # Если переданные данные не соответствуют требованиям к полям модели, то формируется текст сообщения
            # об ошибке
            error = 'Форма была неверной'

    form = NoteForm()
    data = {'form': form, 'error': error}
    return render(request, 'create.html', data)


def search(request):
    """Метод для поиска заметки по запросу пользователя"""
    q = request.GET.get('q')
    notes = Note.objects.filter(Q(title__icontains=q) | Q(text__icontains=q))  # Отбираются записи в базе данных,
    # содержащие в поле Название и Текст запрос пользователя
    return render(request, 'search.html', {'notes': notes})  # Передача в шаблон search.html записей из базы
    # данных, соответствующих запросу
