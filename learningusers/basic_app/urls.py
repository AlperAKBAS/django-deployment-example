from django.urls import path, include
from . import views as app_views



urlpatterns = [
    # path('', app_views.home, name='index'),
    path('about/', app_views.about, name='about'),
    path('login/', app_views.user_login, name='login'),
    path('logout/', app_views.user_logout, name='logout'),
    path('register/', app_views.register, name='register'),
]
