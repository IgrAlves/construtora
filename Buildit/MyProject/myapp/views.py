from django.shortcuts import redirect, render
from myapp.models import  *
from myapp.forms import *
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'buildit/index.html',{"card": Produto.objects.all()})

def create(request):
    form = ProdutoForm
    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'item cadastrado com sucesso!')
            return redirect('index')
        
    return render(request, "buildit/adicionar.html", {"forms":form})

def edit(request, id):
    produto = Produto.objects.get(pk=id)
    form = ProdutoForm(instance=produto)
    return render(request, "buildit/update.html",{"form":form, "produto":produto})


def update(request, id):
    try:
        if request.method == "POST":
            produto = Produto.objects.get(pk=id)
            form = ProdutoForm(request.POST, request.FILES, instance=produto)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'item foi alterada com sucesso!')
                return redirect('index')
    except Exception as e:
        messages.error(request, e)
        return redirect('index')
            

def read(request, id):
    produto = Produto.objects.get(pk=id)
    return render(request, "buildit/read.html", {"produto":produto})

def delete(request, id):
    produto = Produto.objects.get(pk=id)
    produto.delete()
    messages.success(request, 'item foi deletada com sucesso!')
    return redirect('index')

def listar(request):
    return render(request, 'buildit/listar.html',{"cards": Produto.objects.all()})
