
from django.shortcuts import render
from . models import Projects
from django.views.generic import ListView, DetailView

class ProjectsDetailView(DetailView):
    model = Projects

class ProjectsListView(ListView):
    model = Projects
    ordering = ['-date_create']
