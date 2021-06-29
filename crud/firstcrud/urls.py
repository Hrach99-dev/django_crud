from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('delete', delete, name='delete'),
    path('update', update, name='update'), 
]