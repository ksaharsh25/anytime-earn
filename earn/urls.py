from django.urls import path
from .views import *
urlpatterns=[
    path('register',register,name="register"),
    path('login',login,name="login"),
    path('custom',custom_user,name="custom_user"),
    path('advisor',advisor,name="advisor"),

]