
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('Produto/<int:Produto_id>', views.details, name='details'),
]