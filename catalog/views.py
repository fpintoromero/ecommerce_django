from django.shortcuts import render, get_object_or_404
from catalog.models import Category, Subcategory, Product, Brand, Slider, Image, Product_Image
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
import django_filters




def view_index(request):
    categories = Category.objects.filter(status_category='true')
    subcategories = Subcategory.objects.filter(status_subcategory='true')
    products = Product_Image.objects.filter(Q(product_pi__rating_product__gt=3) & Q(image_pi__sort_order_image=0))
    sliders = Slider.objects.filter(status_slider='true')
    sliders.order_by('sort_order_slider')
    return render(request, 'index.html', {'products':products, 'subcategories':subcategories, 'sliders':sliders, 'categories':categories})




def subcategory(request, slug):
    categories = Category.objects.filter(status_category='true')
    subcategories = Subcategory.objects.filter(status_subcategory='true')
    subcategory = get_object_or_404(Subcategory, slug_subcategory=slug)
    product = Product_Image.objects.filter(Q(product_pi__subcategory_product__id=subcategory.pk) & Q(image_pi__sort_order_image=0))
    paginator = Paginator(product, 9)


    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

    
    return render(request, 'category.html', {'products':products, 'subcategories':subcategories, 'subcategory':subcategory, 'product':product, 'categories':categories})

def product_detail(request, slug):
    categories = Category.objects.filter(status_category='true')
    subcategories = Subcategory.objects.filter(status_subcategory='true')
    product = get_object_or_404(Product_Image, product_pi__slug_product=slug)
    products = Product_Image.objects.filter(Q(product_pi__rating_product__gt=3) & Q(image_pi__sort_order_image=0))
    return render(request, 'product.html', {'product': product, 'subcategories':subcategories, 'products':products, 'categories':categories})


