from django.urls import path
from . import views

urlpatterns = [
    path('', views.GroomingServiceListView.as_view(), name='services'),
    path('add/', views.AddServiceView.as_view(), name='add_service'),
    path('edit/<int:pk>/', views.EditServiceView.as_view(), name='edit_service'),
    path('delete/<int:pk>/', views.DeleteServiceView.as_view(), name='delete_service'),
]