from unicodedata import category
from django.shortcuts import get_object_or_404, render, redirect
from .models import Product, Web
from .models import ReviewRating
from marks.models import MarkItem
from marks.views import _mark_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from .forms import ReviewForm
from django.contrib import messages



from category.models import category

# Create your views here.
def store(request,category_slug=None):
    categories = None
    products = None
    

    if category_slug!= None:
        categories = get_object_or_404(category, slug = category_slug)
        products = Product.objects.filter(category = categories, is_available=True)
        paginator = Paginator(products, 100)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('-tmdb')
        paginator = Paginator(products, 100)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()


    context = { 
        'products': paged_products,
        'product_count' : product_count,
    }
    return render(request, 'store.html', context)



def product_detail(request, category_slug, product_slug):
    try: 
        single_product = Product.objects.get(category__slug = category_slug, slug=product_slug)
        in_mark = MarkItem.objects.filter(mark__mark_id = _mark_id(request), product=single_product).exists()


    except Exception as e:
       raise e

    reviews = ReviewRating.objects.filter(product_id=single_product.id, status=True)

    context = {
           'single_product':single_product,
           'in_mark'       :in_mark,
           'reviews'       : reviews,
       }
    return render(request, 'product-detail1.html', context)

def web_detail(request, category_slug, web_slug):
    try: 
        single_web = Web.objects.get(category__slug = category_slug, slug=web_slug)
        in_mark = MarkItem.objects.filter(mark__mark_id = _mark_id(request), web=single_web).exists()


    except Exception as e:
       raise e

    reviews = ReviewRating.objects.filter(product_id=single_web.id, status=True)

    context = {
           'single_web'    :single_web,
           'in_mark'       :in_mark,
           'reviews'       : reviews,
       }
    return render(request, 'series-detail.html', context)

def genres(request):
    return render(request,'category.html')

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains= keyword) | Q(product_name__icontains= keyword ) | Q(product_actor1__icontains= keyword ) | Q(product_actor2__icontains= keyword ) | Q(product_actor3__icontains= keyword ) | Q(product_actor4__icontains= keyword ) | Q(product_actor5__icontains= keyword )| Q(product_actor6__icontains= keyword ))
            product_count = products.count()
        context ={
            'products': products,
            'product_count': product_count,
        }
    return render(request, 'store.html', context)


def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Thank you! Your review has been updated.')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thank you! Your review has been submitted.')
                return redirect(url)
