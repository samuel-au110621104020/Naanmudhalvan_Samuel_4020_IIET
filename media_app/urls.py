from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexPage),
    path('allsongs/',views.allsongs),
]