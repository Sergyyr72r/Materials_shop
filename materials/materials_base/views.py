from django.shortcuts import render
from .models import Material


def index(request):
    template='materials_base/index.html'
    base=Material.objects.all()
    content={
        'base' : base
    }
    return render(request, template, content)

def group(request, slug):
    template='materials_base/index.html'
    return render(request, template, slug)