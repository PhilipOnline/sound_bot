from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def home(request):
    return render(request, 'home/home.html')
# Create your views here.


def ProductList(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'home/product_list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })
# Страница товара
def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request, 'home/product_detail.html', {'product': product})