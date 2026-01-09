from .views import front, sign_in, home, signout
from django.urls import path

urlpatterns = [path("", front, name='front'),
path('sign_in/', sign_in),
path('home/', home),
path('signout/', signout),
]
