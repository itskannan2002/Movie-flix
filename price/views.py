from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomerForm
from django.contrib import messages, auth




from .models import Priceplan, Order
import datetime


# Create your views here.
def subplan(request):
    return render(request, 'pricing/price.html')

def get_queryset(self):
        return Priceplan.objects

def payment_detail(request, Priceplan_slug ):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        email = request.POST['email']
        user = auth.authenticate(email=email)
        

    current_user = request.user

            # If the cart count is less than or equal to 0, then redirect back to shop
    try: 
        single_payments = Priceplan.objects.get( slug=Priceplan_slug)
        
    except Exception as e:
        raise e

    form = CustomerForm()

    

    context = {'form':form,
    'single_payments': single_payments,
    }
    return render(request, 'payment/payment_basic.html', context)
	
    


@login_required(login_url = 'login')
def basic(request):
    
    return render(request, 'payment/payment_basic.html')


@login_required(login_url = 'login')
def saver(request):
    return render(request, 'payment/payment_basic.html')

@login_required(login_url = 'login')
def premimum(request):
    return render(request, 'payment/payment_basic.html')
