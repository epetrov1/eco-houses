from django.urls import path
from .views import PartnersDetailView, PartnersListView

urlpatterns = [
    path('<slug:slug>/', PartnersDetailView.as_view(), name="detail_partners"),
    path('', PartnersListView.as_view(), name="partners_list"),
]