from django.shortcuts import render

# Create your views here.
from .models import Finch
from django.views.generic.edit import CreateView, UpdateView, DeleteView



# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finch_index(request):
  finch = Finch.objects.all()
  return render(request, 'finch/index.html', { 'finch': finch })

def finch_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  return render(request, 'finch/detail.html', { 'finch': finch })

class FinchCreate(CreateView):
  model = Finch
  fields = "__all__"

class FinchUpdate(UpdateView):
  model = Finch
  fields = ['breed', 'description', 'age']



class FinchDelete(DeleteView):
    model = Finch
    success_url= '/finch/'