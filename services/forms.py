from django import forms
from .models import Testimonial, GroomingService


class GroomingServiceForm(forms.ModelForm):
    """
    Form for adding and updating grooming services.
    """
    class Meta:
        model = GroomingService
        fields = '__all__'


class TestimonialForm(forms.ModelForm):
    """
    Form for customers to submit testimonials.
    """
    class Meta:
        model = Testimonial
        fields = '__all__'

class TestimonialUpdateForm(forms.ModelForm):
    """
    Form for customers to update their testimonials.
    """
    class Meta:
        model = Testimonial
        fields = ['body']