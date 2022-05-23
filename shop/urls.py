from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
    # /shop/
    path('', views.IndexView.as_view(), name='index'),

]