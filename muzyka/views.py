import musicbrainzngs
import ssl
from django.core.checks import messages
from django.db.models import Q, Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import SignUpForm, LoginForm
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from GPSPhoto import gpsphoto
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def error_page(request):
    return render(request, 'error_page.html')

def post_list(request, category_slug=None):

    try:
        posts_list = Galeria.objects.all()
        query = request.GET.get('q')
        if query:
            posts_list = Galeria.objects.filter(
                Q(nazwa__icontains=query) | Q(opis__icontains=query)
            ).distinct()
        paginator = Paginator(posts_list.filter(user=request.user), 10)  # 10 posts per page
        page = request.GET.get('page')
        ile = posts_list.filter(user=request.user).count
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        category = None

        categories = Category.objects.all()

        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)

        categories_ile = Galeria.objects.values('category__name').annotate(count=Count('category__name'))
        context = {
            'posts': posts,
            'ile': ile,
            'categories': categories,
            'category': category,
            'categories_ile': categories_ile,
        }


        return render(request, "search.html", context)
    except Exception as ex:
        return redirect(reverse('error'))



def post_list_bez_user(request, category_slug=None):


        posts_list = Galeria.objects.all()
        query = request.GET.get('q')
        if query:
            posts_list = Galeria.objects.filter(
                Q(nazwa__icontains=query) | Q(opis__icontains=query)
            ).distinct()
        paginator = Paginator(posts_list,10)
        page = request.GET.get('page')
        ile = posts_list.count
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        category = None

        categories = Category.objects.all()

        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)

        categories_ile = Galeria.objects.values('category__name').annotate(count=Count('category__name'))
        context = {
            'posts': posts,
            'ile': ile,
            'categories': categories,
            'category': category,
            'categories_ile': categories_ile,
        }


        return render(request, "search_bez_user.html", context)







def post_list_widok_usera(request, category_slug=None):


        posts_list = UlubionyAlbum.objects.select_related()

        query = request.GET.get('q')
        if query:
            posts_list = UlubionyAlbum.objects.filter(
                Q(nazwa__icontains=query) | Q(opis__icontains=query)
            ).distinct()
        paginator = Paginator(posts_list.filter(user=request.user), 10)  # 10 posts per page
        page = request.GET.get('page')
        ile = posts_list.filter(user=request.user).count
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        category = None

        categories = Category.objects.all()

        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)

        categories_ile = Galeria.objects.values('category__name').annotate(count=Count('category__name'))
        context = {
            'posts': posts,
            'ile': ile,
            'categories': categories,
            'category': category,
            'categories_ile': categories_ile,
        }


        return render(request, "widok_user_albumy.html", context)










def fotopage(request, slug, category_slug=None):
    post = Galeria.objects.get(slug=slug)
    slug=post.slug
    kiedy = post.data
    kiedy = kiedy.replace(':', '-')
    category = None
    categories = Category.objects.all()
    story = Galeria.objects.all()
    if request.method == 'POST':
        if 'dodaj' in request.POST:
            if UlubionyAlbum.objects.filter(albumy=post).exists():
                return render(request, 'foto.html', {'post': post,

                                                     'categories': categories,
                                                     'category': category,
                                                     'kiedy': kiedy,
                                                     'story': story,
                                                     'slug': slug})


            else:
                create=UlubionyAlbum.objects.create(user= User.objects.get(pk=request.user.id),albumy=post)
                create.save()

        if 'usun' in request.POST:
            if UlubionyAlbum.objects.filter(albumy=post).exists():
                instance = UlubionyAlbum.objects.get(albumy=post)
                instance.delete()

            else:
                return render(request, 'foto.html', {'post': post,

                                                     'categories': categories,
                                                     'category': category,
                                                     'kiedy': kiedy,
                                                     'story': story,
                                                     'slug': slug})



    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        story = story.filter(category=category)

    return render(request, 'foto.html', {'post': post,

                                         'categories': categories,
                                         'category': category,
                                         'kiedy': kiedy,
                                         'story': story,
                                         'slug': slug})


def metadane(request):
    fot = UploadedImage.objects.all()
    return render(request, "pierwsza.html", {"fot": fot})


def kategorie(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    query = request.GET.get('q')
    story = Galeria.objects.filter(
        Q(nazwa__icontains=query, user=request.user)).distinct()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        story = story.filter(category=category)

    return render(request, 'kategorie.html', {'categories': categories,
                                              'category': category,
                                              'story': story,
                                              })


def story_detail(request, slug):
    story = Galeria.objects.get(slug=slug)
    return render(request, 'foto.html', {'story': story})


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.photo_user = request.FILES['photo_user']
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('register')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})





from django.shortcuts import render, redirect
from . import forms
from . import models
from django.http import HttpResponse


def get_question(request):
    if request.method == 'POST':
        form = forms.QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('../searchbar/')  # or you redirect anywhere you want to
    else:
        form = forms.QuestionForm(request.POST, request.FILES)

    return render(request, 'formularz_dodania.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('login')


