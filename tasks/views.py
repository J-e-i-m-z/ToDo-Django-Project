from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.

def index(request):
    task = Task.objects.all()

    form = TaskForm()

    context = {'tasks': task, 'form': form}
    return render(request, 'tasks/list.html', context)

