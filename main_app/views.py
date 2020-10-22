from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game, Accessory
from .forms import PlayingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class GameList(ListView):
    model = Game

class GameDetail(DetailView):
    model = Game

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['playing_form'] = PlayingForm()
        return context

class GameCreate(CreateView):
    model = Game
    fields = '__all__'

class GameUpdate(UpdateView):
    model = Game
    fields = ['console', 'description', 'year']

class GameDelete(DeleteView):
    model = Game
    success_url = '/games/'

class AccessoryList(ListView):
    model = Accessory

class AccessoryDetail(DetailView):
    model = Accessory

class AccessoryCreate(CreateView):
    model = Accessory
    fields = '__all__'

class AccessoryUpdate(UpdateView):
    model = Accessory
    fields = ['description']

class AccessoryDelete(DeleteView):
    model = Accessory
    success_url = '/accessories/'
