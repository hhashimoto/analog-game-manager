from django.shortcuts import render

from app.models import Item

def detail(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'detail.html', {'item': item})
