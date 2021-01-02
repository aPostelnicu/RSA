from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('encryption/', encryption),
    path('decryption/', decryption),
    path('encryption/resultE/', resultE),
    path('decryption/resultD/', resultD)
]
