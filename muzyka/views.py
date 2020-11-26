from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, request
from django.views import View
from pip._vendor.msgpack.fallback import xrange

from .models import Zespoly
from django.shortcuts import render
from .models import Zespoly
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm
from PIL import Image
from PIL.ExifTags import TAGS





def searchbar(request):
    if request.method == "GET":
        search = request.GET.get('search')
        post = Zespoly.objects.all().filter(nazwa=search)
        return render(request, 'search.html', {"post": post})



def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')



def fotopage(request, slug):
    post = Zespoly.objects.get(slug=slug)
    return render(request, 'foto.html', {'post': post })


def posts_list(request):
    all_posts = Zespoly.objects.all()
    return render(request,
                  "posts_list.html",
                  context = {"all_posts": all_posts})

def posts_detail(request, slug):
    unique_slug = get_object_or_404(Zespoly, slug = slug)
    return render(request, "posts_detail.html", {"post": unique_slug})


def metadane(request):
    fot = UploadedImage.objects.all()
    return render(request, "pierwsza.html", {"fot": fot})

def kategorie(request):
    kat = Zespoly.objects.all()
    return render(request, "kategorie.html", {"kat": kat})


def story_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    story = Zespoly.objects.all()
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        story = story.filter(category=category)
    return render(request, 'kategorie.html', {'categories':categories,
                                              'category':category,
                                              'story':story,
                                              })

def story_detail(request,slug):
    story=Zespoly.objects.get(slug=slug)
    return render(request,'kategorie_wybor.html',{'story':story})
