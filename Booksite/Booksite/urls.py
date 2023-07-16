"""
URL configuration for Booksite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from books.views import BookViewSet, FantasyViewSet, SiFiViewSet, MagicViewSet, SuperheroViewSet, ClassicsViewSet, \
    YoungAdultViewSet, DystopiaViewSet, HiFiViewSet, MysteryViewSet, EspionageViewSet, ContemporaryViewSet


router = routers.SimpleRouter()
router.register('books', BookViewSet)
router.register('fantasy', FantasyViewSet)
router.register('sifi', SiFiViewSet)
router.register('magic', MagicViewSet)
router.register('superhero', SuperheroViewSet)
router.register('classics', ClassicsViewSet)
router.register('youngadult', YoungAdultViewSet)
router.register('dystopia', DystopiaViewSet)
router.register('hifi', HiFiViewSet)
router.register('mystery', MysteryViewSet)
router.register('espionage', EspionageViewSet)
router.register('contemporary', ContemporaryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
