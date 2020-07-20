from django.shortcuts import render
from django.views.generic import ListView


class LetterListView(ListView):
    model = Letter