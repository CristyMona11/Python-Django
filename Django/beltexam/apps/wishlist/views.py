from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Item, Gifter

def index(request):
    context = {
        'items': Item.objects.all(),
        'users': Gifter.objects.all()
    }
    return render(request, 'wishlist/index.html', context)

def add(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'wishlist/add_item.html', context)

def add_item(request):
    if request.method == 'POST':
        server_item = request.POST['item']

        is_valid=True

        if len(server_item) < 3 or len(server_item)< 1:
            messages.error(request, 'Item name too short!!!')
            is_valid=False
            return redirect('wish:add')
        if is_valid:
            item = Item.objects.create(name=server_item)
            return redirect('wish:home')
    context = {
        'items': Item.objects.filter(),
    }
    return render(request, 'wishlist/add_item.html', context)

def people(request):
    context = {
        'items': Item.objects.filter(),
        'users': Gifter.objects.filter()
    }
    gifter = Gifter.objects.create(giftee_id=item_id, gifter_id=user_id)
    return render(request, 'wishlist/people.html', context)
