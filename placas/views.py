from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.forms import inlineformset_factory
from .models import Placa, Video
from .forms import PlacaForm, VideoForm


VideoFormSet = inlineformset_factory(
    Placa, Video,
    form=VideoForm,
    extra=1,
    can_delete=True,
)


def placa_lista(request):
    qs = Placa.objects.prefetch_related('videos').all()
    q = request.GET.get('q', '').strip()
    tipo = request.GET.get('tipo', '')
    estado = request.GET.get('estado', '')

    if q:
        qs = qs.filter(nombre__icontains=q)
    if tipo:
        qs = qs.filter(tipo=tipo)
    if estado == 'finalizado':
        qs = qs.filter(curso_finalizado=True)
    elif estado == 'en_curso':
        qs = qs.filter(curso_finalizado=False)

    context = {
        'placas': qs,
        'q': q,
        'tipo_actual': tipo,
        'estado_actual': estado,
        'tipos': Placa.TIPO_CHOICES,
    }
    return render(request, 'placas/lista.html', context)


def placa_detalle(request, pk):
    placa = get_object_or_404(Placa, pk=pk)
    return render(request, 'placas/detalle.html', {'placa': placa})


def placa_crear(request):
    if request.method == 'POST':
        form = PlacaForm(request.POST, request.FILES)
        formset = VideoFormSet(request.POST, prefix='videos')
        if form.is_valid() and formset.is_valid():
            placa = form.save()
            formset.instance = placa
            formset.save()
            messages.success(request, f'"{placa.nombre}" agregada correctamente.')
            return redirect('placas:detalle', pk=placa.pk)
    else:
        form = PlacaForm()
        formset = VideoFormSet(prefix='videos')
    return render(request, 'placas/form.html', {'form': form, 'formset': formset, 'titulo': 'Nueva placa'})


def placa_editar(request, pk):
    placa = get_object_or_404(Placa, pk=pk)
    if request.method == 'POST':
        form = PlacaForm(request.POST, request.FILES, instance=placa)
        formset = VideoFormSet(request.POST, instance=placa, prefix='videos')
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.success(request, f'"{placa.nombre}" actualizada.')
            return redirect('placas:detalle', pk=placa.pk)
    else:
        form = PlacaForm(instance=placa)
        formset = VideoFormSet(instance=placa, prefix='videos')
    return render(request, 'placas/form.html', {'form': form, 'formset': formset, 'titulo': f'Editar: {placa.nombre}', 'placa': placa})


def placa_eliminar(request, pk):
    placa = get_object_or_404(Placa, pk=pk)
    if request.method == 'POST':
        nombre = placa.nombre
        placa.delete()
        messages.success(request, f'"{nombre}" eliminada.')
        return redirect('placas:lista')
    return render(request, 'placas/confirmar_eliminar.html', {'placa': placa})
