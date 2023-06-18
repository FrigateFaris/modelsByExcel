from django.shortcuts import render
from modelsApp.models import Product, User


# Create your views here.
def info_product_models(request):
    context = {'products': Product.objects.all()}
    return render(request, 'index.html', context=context)


def info_user_models(request):
    context = {'users': User.objects.all()}
    return render(request, 'index2.html', context=context)
