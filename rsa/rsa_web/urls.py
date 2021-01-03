from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('encryption/', encryption, name="encryption"),
    path('decryption/', decryption, name="decryption"),
    path('encryption/resultE/', resultE),
    path('decryption/resultD/', resultD)
]
