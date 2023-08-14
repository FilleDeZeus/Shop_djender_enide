"""
URL configuration for Shop_djender_enide project.

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
from django.urls import path
from app import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('shoe/', views.shoe, name='shoe'),
    path('shoe/details/<int:id>/', views.shoe_details, name='shoe_details'),

    path('blog/', views.blog, name="blog"),
    path('contact/', views.contact, name="contact"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('error_404/', views.error_404, name="error_404"),
    path('blog_details/', views.blog_details, name="blog_details"),
    path('trackorder/', views.trackorder, name="trackorder"),
    path('about/', views.about, name="about"),
    path('wishlist/<int:shoe_id>/', views.wishlist, name="wishlist"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name="signup"),
]
