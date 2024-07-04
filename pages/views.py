from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.views.generic import DetailView
from .models import Pages
from services.models import Services


class HomeView(TemplateView):
    template_name = "pages/home.html"

def load_nav_obj(request):
    nav_obj = Services.objects.all()
    return {'nav_obj': nav_obj}

#Contact view +sending emails
def contacts(request):
    if request.method == "POST":
        message_name = request.POST['name']
        message_email = request.POST['email']
        message = request.POST['message']

        send_mail(
            message_name, #subject
            message, #message
            message_email, #sender 
            ['office@baugmbh.de'], #receivers
            )        

        return render(request, "pages/contacts.html", {'message_name': message_name})
    else:
        return render(request, "pages/contacts.html")


class PagesDetailView(DetailView):
    model = Pages