from django.urls import path
from .views import index
from random import randrange as rr

urlpatterns = [
    path('', index, kwargs={'tip_index': rr(0, 4)}),
]
