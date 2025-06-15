from django.urls import path
from . import views

urlpatterns = [
    path('', views.collect_data, name='collect_data'),
]