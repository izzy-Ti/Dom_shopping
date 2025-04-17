from django.shortcuts import render
from .models import products

def store(request):
    posts = products.objects.all()
    return render(request, 'store/store.html', {'posts' : posts})
def cart(request):
    return render(request, 'store/store.html')
def checkout(request):
    return render(request, 'store/checkout.html')
