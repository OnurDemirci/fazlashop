from django.shortcuts import render

# Create your views here.
from django.views import generic



class IndexView(generic.ListView):
    template_name = 'shop/index.html'
    context_object_name = 'latest_products'