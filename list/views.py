from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from list.models import Letter


class LetterListView(ListView):
    model = Letter

class LetterCreateView(CreateView):
    model = Letter
    fields = '__all__' #['title', 'contents', 'image']
    template_name = 'list/letter_create.html'
    success_url = reverse_lazy('list:list')

class LetterUpdateView(UpdateView):
    model = Letter
    fields = '__all__'
    template_name_suffix = '_update' #drink_update.html
    success_url = reverse_lazy('list:list')

class LetterDeleteView(DeleteView):
    model = Letter
    success_url = reverse_lazy('list:list')