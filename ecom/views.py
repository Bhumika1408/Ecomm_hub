from django.shortcuts import render
from products.models import Product
def homepage(request):
    product = Product.objects.all()
    return render(request,'home.html',{'item_list':product})


def catch_all_view(request):

    return render(request,'404.html')
