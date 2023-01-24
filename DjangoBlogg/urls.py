
from xml.dom.minidom import Document
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from anvandare import views as anvandare_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #om man inte skriver in något så kommer vi till blogg
    path('', include('blogg.urls')),
    path('registrera/',anvandare_views.registrera,name='registrera'),
    path('profil/',anvandare_views.profil,name='profil'),
    path('loggain/',auth_views.LoginView.as_view(template_name='anvandare/loggain.html'),name='loggain'),
    path('loggaut/',auth_views.LogoutView.as_view(template_name='anvandare/loggaut.html'),name='loggaut'),
    path('loggaut/',auth_views.LogoutView.as_view(template_name='anvandare/loggaut.html'),name='loggaut'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
