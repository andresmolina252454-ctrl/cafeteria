from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def store(request):
    return render(request, 'core/store.html')

def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            return redirect(reverse('contact') + '?OK')

    return render(request, 'core/contact.html', {'form': contact_form})