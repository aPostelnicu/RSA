from django.urls import path
from .views import *

urlpatterns = [
    path('', encryption),
    path('decryption/', decryption),
    path('resultE/', resultE),
    path('resultD/', resultD)
]
