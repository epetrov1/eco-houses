from django.urls import path
from .views import ProjectsDetailView, ProjectsListView

urlpatterns = [
    path('<slug:slug>/', ProjectsDetailView.as_view(), name="detail_projects"),
    path('', ProjectsListView.as_view(), name="projects_list"),
]