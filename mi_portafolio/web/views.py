from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ContactForm
from .forms import ContactFormModelForm

# Create your views here.
def indice(request):
    return render(request, 'index.html', {})


def bienvenido(request):
    return render(request, 'welcome.html', {})

def contacto(request):
    if request.method=='POST':
        form=ContactFormModelForm(request.POST)
        if form.is_valid():
            contact_form=ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito')

    else:
        form=ContactFormModelForm()

    return render(request, 'contacto.html', {'form': form})

def exito(resquest):
    return render(resquest, 'success.html', {})