from django.shortcuts import render, redirect

from shop.forms import ProductModelForm
from shop.models import Product


# Create your views here.

def product_list(request):
    products = Product.objects.all()

    context = {'products': products}

    return render(request, 'shop/home.html', context)


def detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    context = {'product': product}
    return render(request, 'shop/detail.html', context)



def add_product(request):
    form = ProductModelForm()
    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'shop/add-product.html', context)
