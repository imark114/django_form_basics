from django.shortcuts import render
from .forms import contactForm
# Create your views here.
def djangoForm(request):
    form = contactForm()
    return render(request,'home.html', {'form': form})