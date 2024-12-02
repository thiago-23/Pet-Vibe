from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactUs.as_view(), name='contact'),
    path('enquiries/', views.EnquiriesListView.as_view(), name='enquiries'),
    path('enquiries/<int:pk>/', views.EnquiryDetailView.as_view(), name='enquiry_detail'),
    path('enquiries/delete/<int:pk>/', views.DeleteEnquiryView.as_view(), name='delete_enquiry'),
]
