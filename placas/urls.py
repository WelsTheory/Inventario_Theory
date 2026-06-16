from django.urls import path
from . import views

app_name = 'placas'

urlpatterns = [
    path('', views.placa_lista, name='lista'),
    path('nueva/', views.placa_crear, name='crear'),
    path('<int:pk>/', views.placa_detalle, name='detalle'),
    path('<int:pk>/editar/', views.placa_editar, name='editar'),
    path('<int:pk>/eliminar/', views.placa_eliminar, name='eliminar'),
]
