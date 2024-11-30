
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import GroomingService, Testimonial
from .forms import GroomingServiceForm
from django.views import generic
from django.shortcuts import redirect


class GroomingServiceListView(ListView):
    """
    Displays all available grooming services.
    """
    model = GroomingService
    template_name = 'services/services.html'
    context_object_name = 'service_list'


class AddServiceView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    Allows superusers to add a new grooming service.
    """
    model = GroomingService
    form_class = GroomingServiceForm
    template_name = 'services/add_service.html'
    success_url = reverse_lazy('services')

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        messages.success(self.request, "Service added successfully.")
        return super().form_valid(form)

class EditServiceView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Allows superusers to edit existing grooming services.
    """
    model = GroomingService
    form_class = GroomingServiceForm
    template_name = 'services/edit_service.html'
    success_url = reverse_lazy('services')

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        messages.success(self.request, "Service updated successfully.")
        return super().form_valid(form)


class DeleteServiceView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Allows superusers to delete grooming services.
    """
    model = GroomingService
    template_name = 'services/delete_service.html'
    success_url = reverse_lazy('services')

    def test_func(self):
        return self.request.user.is_superuser

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Service deleted successfully.")
        return super().delete(request, *args, **kwarg)