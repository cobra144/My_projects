from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import CreateUserForm



def searchbar(request):
    if request.method == "GET":
        search = request.GET.get('search')
        post = Galeria.objects.all().filter(nazwa=search)
        return render(request, 'search.html', {"post": post})




def fotopage(request, slug):
    post = Galeria.objects.get(slug=slug)
    return render(request, 'foto.html', {'post': post })



def posts_detail(request, slug):
    unique_slug = get_object_or_404(Galeria, slug = slug)
    return render(request, "posts_detail.html", {"post": unique_slug})


def metadane(request):
    fot = UploadedImage.objects.all()
    return render(request, "pierwsza.html", {"fot": fot})

def kategorie(request):
    kat = Galeria.objects.all()
    return render(request, "kategorie.html", {"kat": kat})


def story_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    story = Galeria.objects.all()
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        story = story.filter(category=category)
    return render(request, 'kategorie.html', {'categories':categories,
                                              'category':category,
                                              'story':story,
                                              })

def story_detail(request,slug):
    story=Galeria.objects.get(slug=slug)
    return render(request,'kategorie_wybor.html',{'story':story})
