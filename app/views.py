from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class IndexView(ListView):
    model = Item
    template_name = "app/index.html"
    login_url = '/accounts/login/'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'app/product.html'
    login_url = '/accounts/login/'
