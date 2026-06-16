from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Componente
from .forms import ComponenteForm


def componente_lista(request):
    qs = Componente.objects.all()
    q = request.GET.get('q', '').strip()
    categoria = request.GET.get('categoria', '')

    if q:
        qs = qs.filter(nombre__icontains=q) | qs.filter(valor__icontains=q)
    if categoria:
        qs = qs.filter(categoria=categoria)

    context = {
        'componentes': qs,
        'q': q,
        'categoria_actual': categoria,
        'categorias': Componente.CATEGORIA_CHOICES,
    }
    return render(request, 'componentes/lista.html', context)


def componente_crear(request):
    if request.method == 'POST':
        form = ComponenteForm(request.POST)
        if form.is_valid():
            componente = form.save()
            messages.success(request, f'"{componente}" agregado.')
            if 'agregar_otro' in request.POST:
                return redirect('componentes:crear')
            return redirect('componentes:lista')
    else:
        form = ComponenteForm()
    return render(request, 'componentes/form.html', {'form': form, 'titulo': 'Nuevo componente'})


def componente_editar(request, pk):
    componente = get_object_or_404(Componente, pk=pk)
    if request.method == 'POST':
        form = ComponenteForm(request.POST, instance=componente)
        if form.is_valid():
            form.save()
            messages.success(request, f'"{componente}" actualizado.')
            return redirect('componentes:lista')
    else:
        form = ComponenteForm(instance=componente)
    return render(request, 'componentes/form.html', {'form': form, 'titulo': f'Editar: {componente}', 'componente': componente})


def componente_eliminar(request, pk):
    componente = get_object_or_404(Componente, pk=pk)
    if request.method == 'POST':
        nombre = str(componente)
        componente.delete()
        messages.success(request, f'"{nombre}" eliminado.')
        return redirect('componentes:lista')
    return render(request, 'componentes/confirmar_eliminar.html', {'componente': componente})
