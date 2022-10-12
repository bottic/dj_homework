from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'name')
    if sort == 'name':
        context = {'phones': Phone.objects.all().order_by(sort)}
    if sort == 'min_price':
        context = {'phones': Phone.objects.all().order_by('price')}
    if sort == 'max_price':
        context = {'phones': Phone.objects.all().order_by('-price')}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
