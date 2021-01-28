from django.shortcuts import render

# Create your views here.

def index_view(request):
    context = {}
    return render(request, 'main/main.html', context)

def dogs_view(request):
    context = {}
    return render(request, 'main/dogs.html', context)

def cats_view(request):
    context = {}
    return render(request, 'main/cats.html', context)

def rodents_view(request):
    context = {}
    return render(request, 'main/rodents.html', context)

def fish_view(request):
    context = {}
    return render(request, 'main/fish.html', context)

def birds_view(request):
    context = {}
    return render(request, 'main/birds.html', context)

def reptiles_view(request):
    context = {}
    return render(request, 'main/reptiles.html', context)

def test_view(request):
    context = {}
    return render(request, 'main/test.html', context)


