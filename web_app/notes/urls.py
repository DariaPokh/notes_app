from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NoteDetailView.as_view(), name='note_detail'),
    path('<int:pk>/update', views.NoteUpdateView.as_view(), name='note_update'),
    path('<int:pk>/delete', views.NoteDeleteView.as_view(), name='note_delete'),
    path('search/', views.search, name='search'),
]
