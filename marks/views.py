from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .models import Mark, MarkItem
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from marks.models import MarkItem
from django.contrib.auth.decorators import login_required





# Create your views here.
def _mark_id(request):
    mark = request.session.session_key
    if not mark:
        mark = request.session.create()
    return mark



# increasing the marl items in the mark page 
@login_required(login_url = 'login')
def add_mark(request, product_id):
    current_user = request.user
    product = Product.objects.get(id=product_id) # get the product
    if current_user.is_authenticated:
        product_variation = []
        if request.method == 'POST':
            for item in request.POST:
                key = item
                value = request.POST[key]
        
                try:
                    pass
                except:
                    pass

        is_mark_item_exists = MarkItem.objects.filter(product=product, user=current_user).exists()
        if is_mark_item_exists:
            pass
        else:
            mark_item = MarkItem.objects.create(
                product = product,
                quantity = 1,
                user = current_user,
            )
            
            mark_item.save()
        return redirect('mark')
    
    # If the user is not authenticated
    else:
        product_variation = []
        if request.method == 'POST':
            for item in request.POST:
                key = item
                value = request.POST[key]

                try:
                    pass
                except:
                    pass


        try:
            mark = Mark.objects.get(mark_id=_mark_id(request)) # get the cart using the cart_id present in the session
        except Mark.DoesNotExist:
            mark = Mark.objects.create(
                mark_id = _mark_id(request)
            )
        mark.save()

        is_mark_item_exists = MarkItem.objects.filter(product=product, mark=mark).exists()
        if is_mark_item_exists:
            mark_item = MarkItem.objects.filter(product=product, mark=mark)
            # existing_variations -> database
            # movie_id -> database
            ex_var_list = []
            id = []
            for item in mark_item:
                
                id.append(item.id)

            print(ex_var_list)

            if product_variation in ex_var_list:
                index = ex_var_list.index(product_variation)
                item_id = id[index]
                item = MarkItem.objects.get(product=product, id=item_id)
                item.quantity += 1
                item.save()

            else:
                item = MarkItem.objects.create(product=product, quantity=1, mark=mark)
                if len(product_variation) > 0:
                    item.variations.clear()
                    item.variations.add(*product_variation)
                item.save()
        else:
            mark_item = MarkItem.objects.create(
                product = product,
                quantity = 1,
                mark = mark,
            )
            if len(product_variation) > 0:
                mark_item.variations.clear()
                mark_item.variations.add(*product_variation)
            mark_item.save()
        return redirect('mark')



def remove_mark(request, product_id, mark_item_id):
    
    product = get_object_or_404(Product, id = product_id)
    try:
        if request.user.is_authenticated:
            mark_item = MarkItem.objects.get(product=product, user=request.user, id=mark_item_id)
        else:
            mark = Mark.objects.get(mark_id = _mark_id(request))
            mark_item = MarkItem.objects.get(product = product, mark = mark, id=mark_item_id)
 
        if mark_item.quantity >1:
            mark_item.quantity -=1
            mark_item.save()
        else:
            mark_item.delete()
    except: 
        pass
    return redirect('mark')

def mark(request, total = 0 , quantity = 0, mark_items = None):

    try:
        
        grand_total = 0
        if request.user.is_authenticated:
            mark_items = MarkItem.objects.filter(user=request.user, is_active=True)
        else:
            mark = Mark.objects.get(mark_id = _mark_id(request))
            mark_items = MarkItem.objects.filter(mark=mark, is_active=True)
        for mark_item in mark_items:
            total +=  (mark_item.quantity)
            quantity += mark_item.quantity

        grand_total = total
    except ObjectDoesNotExist:
        pass # just ignore 

    context = {
        'total': total,
        'quantity': quantity,
        'mark_items': mark_items,
        'grand_total': grand_total,
        
    }


    return render(request, 'mark.html', context)