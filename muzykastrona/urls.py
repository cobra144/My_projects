from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    path('muzyka/', include('muzyka.urls')),
    path('admin/', admin.site.urls,),
    #path('api/', include('muzyka.urls'))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

