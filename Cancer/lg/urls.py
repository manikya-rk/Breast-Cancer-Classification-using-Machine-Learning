from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='homepage'),
    path('input/', views.input, name='input'),
    path('output/', views.output, name='output')
]
