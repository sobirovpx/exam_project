from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect

from shop.forms import ProductModelForm, CommentModelForm, OrderModelForm
from shop.models import Product, Category, Comment


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
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)

    context = {'product': product,

               'related_products': related_products
               }
    return render(request, 'shop/detail.html', context)


def category_detail(request, category_id):
    category = Category.objects.get(pk=category_id)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()

    return render(request, 'shop/home.html', {'categories': categories, 'products': products, 'category': category})





@csrf_protect
def add_comment(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)

            comment.product = product
            comment.save()
            print('Save Done ! ')
            return redirect('product_detail', product_id)
    else:
        form = CommentModelForm(request.GET)
        print('Get method running')

    return render(request, 'shop/detail.html', {'form': form, 'product': product})


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


def search(request):
    query = request.GET.get('query')
    products = []
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'shop/home.html', {'products': products})

def order(request):
    if request.method == 'POST':
        form = OrderModelForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect('detail')
        else:
            form = OrderModelForm()
        return render(request, 'shop/detail.html', {'form': form})


def page_view(request):
    object_list = Product.objects.all()
    paginator = Paginator(object_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'shop/home.html', {'page_obj': page_obj})
