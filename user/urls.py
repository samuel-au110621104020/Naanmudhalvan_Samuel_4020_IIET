from django.urls import path
from . import views

urlpatterns = [
    path('register',views.new_register,name="register"),
    path('login',views.new_login,name="login"),
    path('logout',views.logout,name="logout"),

]