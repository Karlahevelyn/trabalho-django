from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('login/', views.login, name='login'),
    path('roupas/', views.roupas, name='roupas'),
    path('femininas/', views.femininas, name='femininas'),
    path('masculinas/', views.masculinas, name='masculinas'),
]

urlpatterns = [
    path('pesquisar/', views.pesquisar, name='pesquisar'),
    # outras URLs...
]

urlpatterns = [
    path('pesquisar/', views.pesquisar, name='pesquisar'),
    # outras URLs...
]

urlpatterns = [
    path('login/', views.login_view, name='login'),
    # outras URLs...
]
