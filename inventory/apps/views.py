from django.shortcuts import render, redirect, get_object_or_404
from .models import Category,Product
from .forms import CategoryForm,ProductForm


def category_list(request):
    categories = Category.objects.all()

    return render(
        request,
        'apps/category_list.html',
        {'categories': categories}
    )


def category_create(request):
    form = CategoryForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('category_list')

    return render(
        request,
        'apps/category_form.html',
        {'form': form}
    )


def category_update(request, id):
    category = get_object_or_404(Category, id=id)

    form = CategoryForm(
        request.POST or None,
        instance=category
    )

    if form.is_valid():
        form.save()
        return redirect('category_list')

    return render(
        request,
        'apps/category_form.html',
        {'form': form}
    )


def category_delete(request, id):
    category = get_object_or_404(Category, id=id)

    if request.method == 'POST':
        category.delete()
        return redirect('category_list')

    return render(
        request,
        'apps/category_delete.html',
        {'category': category}
    )
def product_list(request):
    products = Product.objects.all()

    return render(
        request,
        'apps/product_list.html',
        {'products': products}
    )


def product_create(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('product_list')

    return render(
        request,
        'apps/product_form.html',
        {'form': form}
    )


def product_update(request, id):
    product = get_object_or_404(Product, id=id)

    form = ProductForm(
        request.POST or None,
        instance=product
    )

    if form.is_valid():
        form.save()
        return redirect('product_list')

    return render(
        request,
        'apps/product_form.html',
        {'form': form}
    )


def product_delete(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('product_list')

    return render(
        request,
        'apps/product_delete.html',
        {'product': product}
    )
def product_list(request):
    products = Product.objects.all()

    return render(
        request,
        'apps/product_list.html',
        {'products': products}
    )