from django.shortcuts import render
from django.http import HttpResponse

from .models import Item


def index(request):
    items = Item.objects.order_by('-created_at')
    resp_text = '<br>'.join([item.name for item in items])
    return HttpResponse(resp_text)


def register(request):
    return render(request, 'register.html', {})
