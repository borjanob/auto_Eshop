"""
URL configuration for auto_Eshop project.

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
from auto_EshopApp.views import signUp,home,login_func,logout_func,vehicles,add_post,details,wishlist
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/",signUp,name='signUp'),
    path('',home,name='home'),
    path('home/',home,name='home'),
    path('login/',login_func,name='login'),
    path('login/<message>/',login_func,name='login'),
    path('logout/',logout_func,name='logout'),
    path('vehicles/',vehicles,name='vehicles'),
    path('add-post/',add_post,name='add-post'),
    path('details/<int:id>/',details,name='details'),
    path('wishlist/',wishlist,name='wishlist'),
    path('wishlist/<id>',wishlist,name='wishlist')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
