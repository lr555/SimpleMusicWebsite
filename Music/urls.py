"""Music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('artist/', include(('artist.urls', 'artist'), namespace='artist')),
    path('album/', include(('album.urls', 'album'), namespace='album')),
    path('playlist/', include(('playlist.urls', 'playlist'), namespace='playlist')),
    path('song/', include(('song.urls', 'song'), namespace='song')),
    path('user/', include(('user.urls', 'user'), namespace='user')),
    path('search/',include(('search.urls','search'),namespace='search')),
    path('register/',include(('register.urls','register'),namespace='register')),
    path('login/',include(('login.urls','login'),namespace='login')),
    path('logout/',include(('logout.urls','logout'),namespace='logout')),
    path('', include(('home.urls', 'home'), namespace='home')),
]
