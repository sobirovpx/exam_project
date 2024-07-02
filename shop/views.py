from django.shortcuts import render, redirect

from shop.forms import ProductModelForm
from shop.models import Product, Category


# Create your views here.

def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    context = {
        # 'categories': categories,
        'products': products
               }

    return render(request, 'shop/home.html', context, )


def detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    context = {'product': product}
    return render(request, 'shop/detail.html', context)


def category_detail(request, category_id):
    category = Category.objects.get(pk=category_id)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'shop/home.html', {'categories': categories, 'products': products, 'category': category})


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
