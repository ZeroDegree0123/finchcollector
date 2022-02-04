from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Finch:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age
finches = [
    Finch('sal', 'Double-Barred Finch',  'has two beaks', 4),
    Finch('lard', 'The Bengalese Finch',  'can sing', 5),
    Finch('bobby', 'Star Finch', 'Has a scarlet bill and a yellow belly', 7),
    Finch('marvin', 'Strawberry Finch',  'Bright Red like the Burning SUN', 2),
]

def home(request):
    return HttpResponse('<h1>Home Page</h1>')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {'finches': finches })