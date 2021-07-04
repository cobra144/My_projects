from django.db.models import Q, Count, Avg
from django.shortcuts import get_object_or_404
from .forms import SignUpForm
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from . import forms


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
        paginator = Paginator(posts_list, 10)  # 10 posts per page
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
            'categories_ile': categories_ile}

        return render(request, "search.html", context)
    except Exception as ex:
        return redirect(reverse('error'))


def post_list_bez_user(request, category_slug=None):
    try:
        posts_list = Galeria.objects.all()
        query = request.GET.get('q')
        if query:
            posts_list = Galeria.objects.filter(
                Q(nazwa__icontains=query) | Q(opis__icontains=query)
            ).distinct()
        paginator = Paginator(posts_list, 10)
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
            'categories_ile': categories_ile}

        return render(request, "search_bez_user.html", context)
    except Exception as ex:
        return redirect(reverse('error'))


def PostListWidokUsera(request, category_slug=None):
    try:
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
            'categories_ile': categories_ile}

        return render(request, "widok_user_albumy.html", context)
    except Exception as ex:
        return redirect(reverse('error'))


def fotopage(request, slug):
    post = Galeria.objects.get(slug=slug)
    slug = post.slug
    category = None
    categories = Category.objects.all()
    story = Galeria.objects.all()
    args = dict()
    args['mytext'] = 2
    if OcenaAlbumu.objects.filter(album=post).filter(user=request.user.id):
        ocenionoNa = True
        sredniaOcena = OcenaAlbumu.objects.filter(album=post).aggregate(Avg('ocena'))
        dodaj_ocene = OcenaAlbumu.objects.filter(album=post).filter(user=request.user.id)
        dodaj_ocene = dodaj_ocene.get
        args['mytext'] = 2
        if UlubionyAlbum.objects.filter(albumy=post).filter(user=request.user.id):
            args['mytext'] = 1
        if request.method == 'POST':
            if 'first' in request.POST:
                OcenaAlbumu.objects.filter(user=User.objects.get(pk=request.user.id), album=post).update(ocena=1)
            elif 'second' in request.POST:
                OcenaAlbumu.objects.filter(user=User.objects.get(pk=request.user.id), album=post).update(ocena=2)
            elif 'third' in request.POST:
                OcenaAlbumu.objects.filter(user=User.objects.get(pk=request.user.id), album=post).update(ocena=3)
            elif 'fourth' in request.POST:
                OcenaAlbumu.objects.filter(user=User.objects.get(pk=request.user.id), album=post).update(ocena=4)
            elif 'fifth' in request.POST:
                OcenaAlbumu.objects.filter(user=User.objects.get(pk=request.user.id), album=post).update(ocena=5)
            if 'usun' in request.POST:
                if UlubionyAlbum.objects.filter(albumy=post).exists():
                    instance = UlubionyAlbum.objects.filter(albumy=post)
                    instance.delete()
                    args['mytext'] = 2
            else:
                if request.method == 'POST':
                    if 'dodaj' in request.POST:
                        if UlubionyAlbum.objects.filter(albumy=post).filter(user=request.user.id):
                            pass
                        else:
                            create = UlubionyAlbum.objects.create(user=User.objects.get(pk=request.user.id), albumy=post)
                            create.save()
                            args['mytext'] = 1
        return render(request, 'foto.html', {'post': post,
                                             'categories': categories,
                                             'category': category,
                                             'story': story,
                                             'slug': slug,
                                             'ocenionoNa': ocenionoNa,
                                             'dodaj_ocene': dodaj_ocene,
                                             'sredniaOcena': sredniaOcena,
                                             'args': args})
    else:
        ocenionoNa = True
        sredniaOcena = OcenaAlbumu.objects.filter(album=post).aggregate(Avg('ocena'))
        dodaj_ocene = OcenaAlbumu.objects.filter(album=post).filter(user=request.user.id)
        dodaj_ocene = dodaj_ocene.get
        args['mytext'] = 2
        if UlubionyAlbum.objects.filter(albumy=post).filter(user=request.user.id):
            args['mytext'] = 1
        if request.method == 'POST':
            if 'first' in request.POST:
                create = OcenaAlbumu.objects.create(user=User.objects.get(pk=request.user.id), album=post, ocena=1)
                create.save()
            elif 'second' in request.POST:
                create = OcenaAlbumu.objects.create(user=User.objects.get(pk=request.user.id), album=post, ocena=2)
                create.save()
            elif 'third' in request.POST:
                create = OcenaAlbumu.objects.create(user=User.objects.get(pk=request.user.id), album=post, ocena=3)
                create.save()
            elif 'fourth' in request.POST:
                create = OcenaAlbumu.objects.create(user=User.objects.get(pk=request.user.id), album=post, ocena=4)
                create.save()
            elif 'fifth' in request.POST:
                create = OcenaAlbumu.objects.create(user=User.objects.get(pk=request.user.id), album=post, ocena=5)
                create.save()
            if 'usun' in request.POST:
                if UlubionyAlbum.objects.filter(albumy=post).exists():
                    instance = UlubionyAlbum.objects.filter(albumy=post)
                    instance.delete()
                    args['mytext'] = 2
            else:
                if request.method == 'POST':
                    if 'dodaj' in request.POST:
                        if UlubionyAlbum.objects.filter(albumy=post).filter(user=request.user.id):
                            pass
                        else:
                            create = UlubionyAlbum.objects.create(user=User.objects.get(pk=request.user.id), albumy=post)
                            create.save()
                            args['mytext'] = 1
        return render(request, 'foto.html', {'post': post,
                                             'categories': categories,
                                             'category': category,
                                             'story': story,
                                             'slug': slug,
                                             'ocenionoNa': ocenionoNa,
                                             'dodaj_ocene': dodaj_ocene,
                                             'sredniaOcena': sredniaOcena,
                                             'args': args})


def metadane(request):
    fot = UploadedImage.objects.all()
    return render(request, "pierwsza.html", {"fot": fot})


def kategorie(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    query = request.GET.get('q')
    story = Galeria.objects.filter(
        Q(nazwa__icontains=query)).distinct()
    ile = story.count
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        story = story.filter(category=category)

    return render(request, 'kategorie.html', {'categories': categories,
                                              'category': category,
                                              'story': story,
                                              'ile': ile,
                                              })


def story_detail(request, slug):
    story = Galeria.objects.get(slug=slug)
    return render(request, 'foto.html', {'story': story})


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.photo_user = request.FILES['photo_user']
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('widok_user_albumy')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


def get_question(request):
    if request.method == 'POST':
        form = forms.QuestionForm(request.POST, request.FILES)
        param = request.POST["nazwa"]
        if Galeria.objects.filter(nazwa=param):
            return render(request, "search.html")
        else:
            if form.is_valid():
                Galeria.user = request.user
                form.save()
            return redirect('../searchbar/')
    else:
        form = forms.QuestionForm(request.POST, request.FILES)

    return render(request, 'formularz_dodania.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('login')
