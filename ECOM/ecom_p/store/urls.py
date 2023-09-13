from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
    path('',views.index,name="home"),
    path('collections',views.collections,name="collections"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    

]
