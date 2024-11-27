from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import GroomingService, Testimonial


class GroomingServiceListView(ListView):
    """
    Displays all available grooming services.
    """
    model = GroomingService
    template_name = 'services/services.html'
