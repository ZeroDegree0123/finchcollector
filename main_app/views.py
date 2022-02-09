from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Seed
from .forms import FeedingForm
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
    feeding_form = FeedingForm()
    seeds_ids = finch.seeds.all().values_list('id')
    seeds = Seed.objects.exclude(id__in=seeds_ids)
    return render(request, 'finches/detail.html', {
        'finch': finch,
        'feeding_form': feeding_form,
        'seeds': seeds 
    })

class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'breed', 'description', 'age']

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)   

class SeedList(ListView):
  model = Seed

class SeedDetail(DetailView):
  model = Seed

class SeedCreate(CreateView):
  model = Seed
  fields = '__all__'

class SeedUpdate(UpdateView):
  model = Seed
  fields = ['name', 'price']

class SeedDelete(DeleteView):
  model = Seed
  success_url = '/seeds/'

def assoc_seed(request, finch_id, seed_id):
    Finch.objects.get(id=finch_id).seeds.add(seed_id)
    return redirect('detail', finch_id=finch_id)
    
def unassoc_seed(request, finch_id, seed_id):
    Finch.objects.get(id=finch_id).seeds.remove(seed_id)
    return redirect('detail', finch_id=finch_id)



# finches = [
#     Finch('sal', 'Double-Barred Finch',  'has two beaks', 4),
#     Finch('lard', 'The Bengalese Finch',  'can sing', 5),
#     Finch('bobby', 'Star Finch', 'Has a scarlet bill and a yellow belly', 7),
#     Finch('marvin', 'Strawberry Finch',  'Bright Red like the Burning SUN', 2),
# ]