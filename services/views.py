
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import GroomingService, Testimonial
from .forms import GroomingServiceForm, TestimonialForm, TestimonialUpdateForm
from django.views import generic
from django.shortcuts import redirect
import logging

logger = logging.getLogger(__name__)

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
        return super().delete(request, *args, **kwargs)

class TestimonialListView(ListView):
    """
    Displays approved testimonials.
    """
    model = Testimonial
    template_name = 'services/testimonials.html'
    context_object_name = 'testimonials'

    def get_queryset(self):
        return Testimonial.objects.filter(is_approved=True)


class AddTestimonialView(LoginRequiredMixin, CreateView):
    """
    Allows users to add testimonials.
    """
    model = Testimonial
    form_class = TestimonialForm
    template_name = 'services/add_testimonial.html'
    success_url = reverse_lazy('testimonials')

    def form_valid(self, form):
        form.instance.email = self.request.user.email
        messages.success(self.request, "Your testimonial has been submitted for approval.")
        return super().form_valid(form)


class EditTestimonialView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Allows users to edit their testimonials.
    """
    model = Testimonial
    form_class = TestimonialUpdateForm
    template_name = 'services/edit_testimonial.html'

    def test_func(self):
        testimonial = self.get_object()

        # Ensure the user is logged in and has an email
        if not self.request.user.is_authenticated or not self.request.user.email:
            logger.warning("User is not authenticated or email is missing.")
            return False

        # Compare the user's email with the testimonial's email
        if testimonial.email and self.request.user.email == testimonial.email:
            return True

        logger.warning("Email mismatch or testimonial email is missing.")
        return False

    def form_valid(self, form):
        messages.success(self.request, "Your testimonial has been updated.")
        return super().form_valid(form)



class DeleteTestimonialView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Allows users to delete their testimonials.
    """
    model = Testimonial
    template_name = 'services/delete_testimonial.html'
    success_url = reverse_lazy('testimonials')

    def test_func(self):
        testimonial = self.get_object()
        return self.request.user.email == testimonial.email

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Your testimonial has been deleted.")
        return super().delete(request, *args, **kwargs)