from django.urls import path
from . import views

app_name = 'componentes'

urlpatterns = [
    path('', views.componente_lista, name='lista'),
    path('nuevo/', views.componente_crear, name='crear'),
    path('<int:pk>/editar/', views.componente_editar, name='editar'),
    path('<int:pk>/eliminar/', views.componente_eliminar, name='eliminar'),
]
