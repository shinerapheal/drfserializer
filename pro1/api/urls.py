from django.urls import path
from app1.views import *
from app1 import views

urlpatterns = [
    path('view/',views.view)
]