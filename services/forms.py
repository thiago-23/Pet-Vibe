from django import forms
from .models import Testimonial


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