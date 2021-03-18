from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('gold/<str:location_name>', views.process_money),
    path('reset', views.reset),
]