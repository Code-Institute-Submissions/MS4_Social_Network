from django.shortcuts import render
from .models import Product


def donations(request):
    """
    A view to show all donation options
    """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/donations.html', context)
