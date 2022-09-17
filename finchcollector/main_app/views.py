from django.shortcuts import render, redirect

# Create your views here.
from .models import Finch, Toy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm

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
  print(finch.toys.all().values_list('id'))

  toys_cat_doesnt_have = Toy.objects.exclude(id__in = finch.toys.all().values_list('id'))
  print(toys_cat_doesnt_have)

  feeding_form = FeedingForm()


  return render(request, 'finch/detail.html', {
     'finch': finch,
     'feeding_form': feeding_form,
     'toys': toys_cat_doesnt_have
      })

class FinchCreate(CreateView):
  model = Finch
  fields = "__all__"

class FinchUpdate(UpdateView):
  model = Finch
  fields = ['breed', 'description', 'age']



class FinchDelete(DeleteView):
    model = Finch
    success_url= '/finch/'

def add_feeding(request, finch_id):
  print(request.POST)
  form = FeedingForm(request.POST)
  print(form)

  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('finch_detail', finch_id=finch_id)

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'

def assoc_toy(request, finch_id, toy_id):
  Finch.objects.get(id=finch_id).toys.add(toy_id)
  return redirect('finch_detail', finch_id = finch_id)

def unassoc_toy(request, finch_id, toy_id):
  Finch.objects.get(id=finch_id).toys.remove(toy_id)
  return redirect('finch_detail', finch_id = finch_id)

