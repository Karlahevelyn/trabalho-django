# Rota de referência como trabalhoprogramação.com
from django.urls import path
from app_roupas import views

urlpatterns = [
    path('', views.home, name='home'),
    path('roupas/', views.roupas, name='listagem_roupas')

]
