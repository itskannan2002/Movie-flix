from django.shortcuts import render
from store.models import Product, Web



def home(request):
    products = Product.objects.all().filter(is_available=True)
    webs = Web.objects.all().filter(is_available=True)

    context = { 
        'products': products,
        'webs': webs,


    }
    return render(request,'home.html', context)

def genres(request):
    return render(request,'category.html')
