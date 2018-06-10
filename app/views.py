from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Item
from .forms import ItemForm


def index(request):
    items = Item.objects.order_by('-created_at')
    resp_text = '<br>'.join([item.name for item in items])
    return HttpResponse(resp_text)


def register(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/app/')
    else:
        form = ItemForm()
    return render(request, 'register.html', {'form': form})
