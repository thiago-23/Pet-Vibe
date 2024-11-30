from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    """
    Form for users to submit contact inquiries.
    """
    class Meta:
        model = Contact
        fields = '__all__'