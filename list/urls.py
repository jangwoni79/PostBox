
from django.urls import path
from list.views import LetterListView, LetterCreateView, LetterUpdateView, LetterDeleteView

app_name = 'list'

urlpatterns = [
    path('', LetterListView.as_view(), name = 'list'),
    path('add_letter/', LetterCreateView.as_view(), name = 'add_letter'),
    path('update/<int:pk>/', LetterUpdateView.as_view(), name = 'update'),
    path('delete/<int:pk>/', LetterDeleteView.as_view(), name = 'delete'),
]

