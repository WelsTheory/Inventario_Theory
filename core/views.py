from urllib.parse import urlencode

from django.shortcuts import render, redirect
from django.urls import reverse


def dashboard(request):
    q = request.GET.get('q', '').strip()
    if q:
        url = reverse('componentes:lista') + '?' + urlencode({'q': q})
        return redirect(url)
    return render(request, 'core/dashboard.html')


def agregar(request):
    return render(request, 'core/agregar.html')
