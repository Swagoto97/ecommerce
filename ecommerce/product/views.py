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
    return render(req, 'index1.html', context)
