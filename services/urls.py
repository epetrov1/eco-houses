from django.urls import path
from .views import ServicesDetailView, ServicesListView



urlpatterns = [
    path('<slug:slug>/', ServicesDetailView.as_view(), name="detail_services"),
    path('', ServicesListView.as_view(), name="services_list"),
]