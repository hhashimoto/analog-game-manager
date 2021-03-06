from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from app.models import Item

def index(request):
    items = Item.objects.order_by('-created_at')
    resp_text = '<br>'.join([item.name for item in items])
    return HttpResponse(resp_text)
