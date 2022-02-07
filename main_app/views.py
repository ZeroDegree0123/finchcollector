from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch
# Create your views here.

def home(request):
    return render(request,'base.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', { 'finch': finch })

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

class FinchCreate(UpdateView):
    model = Finch
    fields = ['breed', 'description', 'age']

class FinchCreate(DeleteView):
    model = Finch
    success_url = '/finches/'
    








# finches = [
#     Finch('sal', 'Double-Barred Finch',  'has two beaks', 4),
#     Finch('lard', 'The Bengalese Finch',  'can sing', 5),
#     Finch('bobby', 'Star Finch', 'Has a scarlet bill and a yellow belly', 7),
#     Finch('marvin', 'Strawberry Finch',  'Bright Red like the Burning SUN', 2),
# ]