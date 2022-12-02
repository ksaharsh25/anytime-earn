from django.urls import path
from .views import *
urlpatterns=[
    path('custom',custom_user,name="custom_user"),
    path('advisor',advisor,name="advisor"),
]