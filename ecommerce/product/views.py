from django.shortcuts import render
from .models import products, Catagory

# Create your views here.


def index(req):
    product_list = products.objects.all()
    catagory_list = Catagory.objects.all()
    # print(product_list)
    # print(catagory_list)
    context = {'product_list': product_list,
               'catagory_list': catagory_list,
               }
    # print(context)
    return render(req, 'index.html', context)


def product_details(req, slug):
    item_details = products.objects.get(slug=slug)
    context = {'item_details': item_details, }
    return render(req, 'itemdetails.html', context)
