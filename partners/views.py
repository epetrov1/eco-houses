
from django.shortcuts import render
from . models import Partners
from django.views.generic import ListView, DetailView

class PartnersDetailView(DetailView):
    model = Partners

class PartnersListView(ListView):
    model = Partners
    ordering = ['-date_create']