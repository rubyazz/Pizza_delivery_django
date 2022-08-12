from django.contrib import admin
from django.urls import path, include

from shop import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("cart", views.cart, name= "cart"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
