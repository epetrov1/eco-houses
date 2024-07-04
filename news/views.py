
from django.shortcuts import render
from . models import News
from django.views.generic import ListView, DetailView

class NewsDetailView(DetailView):
    model = News

class NewsListView(ListView):
    model = News
    ordering = ['-date_create']
