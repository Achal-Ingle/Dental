from django.shortcuts import render
from .models import Picture
# Create your views here.
def index(request):

    pics = Picture.objects.all()

    return render(request, "index.html", {'pics': pics})

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    return render(request, "contact.html")

def doctors(request):
    return render(request, "doctors.html")

def blog(request):
    return render(request, "blog.html")

def blog_single(request):
    return render(request, "blog_single.html")

