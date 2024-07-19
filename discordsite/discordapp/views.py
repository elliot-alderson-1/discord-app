from django.shortcuts import render
from .models import Contact
from datetime import date
# Create your views here.
def home(request):
    return render(request, "index.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        contact = Contact(name=name, desc=desc, date = date.today())
        contact.save()

    return render(request, 'index.html')