from django.urls import path
from . import views

urlpatterns = [
    path('paciente/<int:paciente_id>/', views.ver_paciente, name="ver_paciente"),
    path('', views.dashboard, name="dashboard"),
    path('painel/', views.painel, name="painel"),
    path('busca/', views.busca, name='busca')
]