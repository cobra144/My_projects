from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
                  #path('', views.story_list, name='story_list'),
                  path('powitanie/', views.metadane, name="pierwsza"),
                  path('searchbar/',views.searchbar, name="searchbar"),
                  path('foto/<slug:slug>', views.fotopage, name="fotopage"),
                  path('kategorie/', views.story_list, name="kategorie"),
                  path('<slug:category_slug>', views.story_list, name='story_by_category'),
                  path('<int:slug>/', views.story_detail, name='story_detail'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
