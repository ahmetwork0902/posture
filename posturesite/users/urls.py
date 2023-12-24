from django.urls import path
from .import views

from .views import *

app_name = "users"

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),

]