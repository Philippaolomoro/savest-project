from django.urls import path
from . import views

urlpatterns = [
    path('savestpages/', views.home, name='index.html')
]