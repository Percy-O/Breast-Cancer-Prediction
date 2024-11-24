from django.urls import path
from . import views

app_name = 'prediction'

urlpatterns = [
    path('',views.register,name='register'),
    path('login',views.account_login,name='login'),
    path('logout',views.account_logout,name='logout'),
    path('home',views.home,name='home'),
]
