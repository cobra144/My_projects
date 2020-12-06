from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def post_list(request,category_slug=None):
    posts_list = Galeria.objects.all()
    query = request.GET.get('q')
    if query:
        posts_list = Galeria.objects.filter(
            Q(nazwa__icontains=query)
        ).distinct()
    paginator = Paginator(posts_list, 10) # 6 posts per page
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
    story = Galeria.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        story = story.filter(category=category)

    context = {
        'posts': posts,
        'ile': ile,
        'categories': categories,
        'category': category,
        'story': story,

    }
    return render(request, "search.html", context)







def fotopage(request, slug,category_slug=None):
    post = Galeria.objects.get(slug=slug)
    category = None
    categories = Category.objects.all()
    story = Galeria.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        story = story.filter(category=category)


    return render(request, 'foto.html', {'post': post,

        'categories': categories,
        'category': category,
        'story': story, })



def metadane(request):
    fot = UploadedImage.objects.all()
    return render(request, "pierwsza.html", {"fot": fot})

def kategorie(request):
    kat = Galeria.objects.all()
    return render(request, "kategorie.html", {"kat": kat})


def kategorie(request,category_slug=None):
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
    return render(request,'foto.html',{'story':story})




