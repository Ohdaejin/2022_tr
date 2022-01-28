from django.urls import path
from . import views

app_name = 'group'

urlpatterns = [
    path('', views.main, name='main'),
    path('make/', views.make, name='make'),
    path('mine/', views.mine, name='mine'),
]