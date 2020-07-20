
from django.urls import path
from list.views import LetterListView

app_name = 'list'

urlpatterns = [
    path('', LetterListView.as_view(), name = 'list'),
]

