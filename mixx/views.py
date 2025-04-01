from django.shortcuts import render
from .models import Produto
# Create your views here.

def home(request):
    Produtos = Produto.objects.all()
    return render(request, 'home.html', {'Produtos':Produtos})

def details(request, Produto_id):
    Produto = get_object_or_404(Produto, pk=Produto_id)
    return render(request, 'details.html', {'Produto':Produto})