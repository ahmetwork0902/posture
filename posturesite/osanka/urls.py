from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('start/', start, name='start'),
    path('achievements/', achievements, name='achievements'),
    path('start_total_start/', start_total_start, name='start_total_start'),
    # path('start_main_not_authorized/', start_main_not_authorized, name='start_main_not_authorized')
]