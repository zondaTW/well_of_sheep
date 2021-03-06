from django.shortcuts import render
from django.http import HttpResponse
from .models import sheeps_table

# Create your views here.

def table(request):
    sheeps = sheeps_table.objects.order_by('-id').all()[:10]
    return render(request, 'wallofsheep/table.html', {'sheeps': sheeps})

def get_more_tables(request):
    sheeps = sheeps_table.objects.order_by('-id').all()[:10]
    return render(request, 'wallofsheep/get_more_tables.html', {'sheeps': sheeps})
