from django.shortcuts import render

from catalog.models import Product


def index(request):
    context = {
        'products': Product.objects.all()
    }

    for obj in context['products']:
        obj.description = obj.description[:100]

    return render(request, 'catalog/main_menu.html', context)


def about_prod(request, pk):
    context = {
        'products': [Product.objects.get(pk=pk)]
    }
    return render(request, 'catalog/about_prod.html', context)
