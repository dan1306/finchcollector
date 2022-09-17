from django.shortcuts import render, redirect

# Create your views here.
from .models import Finch, Toy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def finch_index(request):
  finch = Finch.objects.all()
  return render(request, 'finch/index.html', { 'finch': finch })

@login_required
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

class FinchCreate(LoginRequiredMixin, CreateView):
  model = Finch
  fields = ['name', 'breed', 'description', 'age']

  def form_valid(self, form):
    form.instance.user = self.request.user  # form.instance is the cat
    return super().form_valid(form)

class FinchUpdate(LoginRequiredMixin, UpdateView):
  model = Finch
  fields = ['breed', 'description', 'age']



class FinchDelete(LoginRequiredMixin, DeleteView):
    model = Finch
    success_url= '/finch/'

@login_required
def add_feeding(request, finch_id):
  print(request.POST)
  form = FeedingForm(request.POST)
  print(form)

  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('finch_detail', finch_id=finch_id)

class ToyList(LoginRequiredMixin, ListView):
  model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy

class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'

@login_required
def assoc_toy(request, finch_id, toy_id):
  Finch.objects.get(id=finch_id).toys.add(toy_id)
  return redirect('finch_detail', finch_id = finch_id)

@login_required
def unassoc_toy(request, finch_id, toy_id):
  Finch.objects.get(id=finch_id).toys.remove(toy_id)
  return redirect('finch_detail', finch_id = finch_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('finch')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)