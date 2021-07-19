from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
from rest_framework import routers

from .views import Apiview

router = routers.DefaultRouter()
router.register('muzyka',Apiview,basename='api_muzyka')

urlpatterns = [
                  path('', views.post_list, name='searchbar'),
                  path('powitanie/', views.metadane, name="pierwsza"),
                  path('searchbar/', views.post_list, name="searchbar"),
                  path('searchbar_bez_user/', views.post_list_bez_user, name="searchbar_bez_user"),
                  path('foto/<slug:slug>', views.fotopage, name="fotopage"),
                  path('kategorie/', views.kategorie, name="kategorie"),
                  path('<slug:category_slug>', views.kategorie, name='story_by_category'),
                  path('foto/<slug:slug>', views.paginacja, name='paginacja'),
                  path('pagination/', views.paginacja, name='pagination'),
                  path('register/', views.register, name='register'),
                  path('login/', auth_views.LoginView.as_view(template_name="login.html",), name="login",),
                  path('formularz/', views.get_question, name='formularz'),
                  path('logout/', views.logoutUser, name="logout"),
                  path('error/', views.error_page, name="error"),
                  path('widok_user_albumy/', views.PostListWidokUsera, name="widok_user_albumy"),
                  path('',include(router.urls))
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
