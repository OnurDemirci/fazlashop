from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
# Create your views here.
from django.views import generic
from .models import Product, Shop
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'shop/index.html'
    context_object_name = 'newest_shops'

    def get_queryset(self):
        return Shop.objects.order_by('-created_date')[:5]

def create_shop(request):
    created_date = request.POST['created_date'] if request.POST['created_date'] else timezone.now()
    try:
        shop_name = request.POST['shop_name']
        shop = Shop.objects.create(shop_name,created_date)
        shop.save()    
        return HttpResponse("Successful")
    except:
        return render(request, 'shop/index.html', {
            'shop' : shop,
            'error_message' : "An error occurred."
        })        

