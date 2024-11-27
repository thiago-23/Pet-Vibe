from django.urls import path
from . import views

urlpatterns = [
    path('', views.GroomingServiceListView.as_view(), name='services'),
]