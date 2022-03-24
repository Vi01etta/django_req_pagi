from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    phone = Phone.objects.all()
    sort = request.GET.get('sort')
    if sort == 'name':
        phone = phone.order_by('name')
    elif sort == 'min_price':
        phone = phone.order_by('price')
    elif sort == 'max_price':
        phone = phone.order_by('-price')

    context = {
        'phones' : phone,
    }
    template = 'catalog.html'

    return render(request, template, context=context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {
        'phone': phone
    }
    return render(request, template, context)

