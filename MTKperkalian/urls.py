from django.contrib import admin
from django.urls import path
from pengertian.views import pengertian
from sifat.views import sifat
from latihan.views import latihan
from profil.views import profil

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pengertian/', pengertian),
    path('sifat/', sifat),
    path('latihan/', latihan),
    path('profil/', profil),
]
