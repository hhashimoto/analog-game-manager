from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from app.forms import ItemForm

def register(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/app/')
    else:
        form = ItemForm()
    return render(request, 'register.html', {'form': form})

