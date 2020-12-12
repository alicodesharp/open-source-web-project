"""Hayyam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Posts.views import Loggin, Register, Welcome, Logout, Profilim, Konular, Konu_Profil, User_List
from Questions import views
from django.conf.urls import url,include




urlpatterns = [

    path('admin/', admin.site.urls),
    path('', Loggin.as_view(), name='karsilama'),
    path('register/', Register.as_view()),
    path('hayyam-anasayfa/', Welcome.as_view()),
    path('log-out/', Logout.as_view()),
    path('profil-sayfam/', Profilim.as_view()),
    path('hayyam-konular/', Konular.as_view()),
    path('konular/<int:id>/', Konu_Profil),
    path('kullanici-listesi/', User_List.as_view()),
    path('soru-coz/',views.soruCoz.as_view()),
    path('test/<int:id>', views.TesteGit),
    path('testi_tamamla/', views.testiTamamla),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)