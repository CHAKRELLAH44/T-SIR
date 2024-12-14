from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.SignupPageAndLogin,name='SignupPageAndLogin'),
    path('account/logout',views.logout_user,name='logout'),
    path('index/',views.HomePage,name='index'),
]
