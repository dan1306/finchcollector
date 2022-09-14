from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


class Finch:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

Finch = [
  Finch('Lolo', 'tabby', 'foul little demon', 3),
  Finch('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Finch('Raven', 'black tripod', '3 legged cat', 4)
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Supposed to be a collector</h1>')

def about(request):
  return render(request, 'about.html')

def finch_index(request):
  return render(request, 'finch/index.html', { 'finch': Finch })