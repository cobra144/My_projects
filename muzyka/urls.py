from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
                  #path('', views.story_list, name='story_list'),
                  path('powitanie/', views.metadane, name="pierwsza"),
                  path('searchbar/',views.post_list, name="searchbar"),
                  path('foto/<slug:slug>', views.fotopage, name="fotopage"),
                  path('kategorie/', views.kategorie, name="kategorie"),
                  path('<slug:category_slug>', views.kategorie, name='story_by_category'),
                  path('foto/<slug:slug>', views.story_detail, name='story_detail'),
                  path('pagination/', views.story_detail, name='pagination'),


              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
