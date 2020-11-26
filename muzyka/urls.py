from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
                  #path('', views.story_list, name='story_list'),
                  path('powitanie/', views.metadane, name="pierwsza"),
                  path('searchbar/',views.searchbar, name="searchbar"),
                  path('register/', views.registerPage, name="register"),
                  path('login/', views.loginPage, name="login"),
                  path('logout/', views.logoutUser, name="logout"),
                  path('foto/<slug:slug>', views.fotopage, name="fotopage"),
                  path('kategorie/', views.story_list, name="kategorie"),
                  path('<slug:category_slug>', views.story_list, name='story_by_category'),
                  path('<int:slug>/', views.story_detail, name='story_detail'),
                  #path('kategorie_wybor/<slug:slug>', views.kategorie_wyb, name="kategorie_wybor"),
                  #path('<slug>', views.fotopage, name="fotopage"),
                  #path("posts/", views.posts_list, name = "posts_list"),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
