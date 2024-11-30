from django.db import models
from services.models import GroomingService
from django.urls import reverse

class Contact(models.Model):
    """ Model for Contact """
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=254, null=False, blank=False)
    enquiry_type = models.ForeignKey(
        GroomingService, on_delete=models.SET_NULL, null=True,
        blank=True, related_name='contact')
    message = models.TextField(max_length=500, default='')
    date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        """Get url after user submits enquiry """
        return reverse('home')

    def __str__(self):
        return f"Enquiry: {self.enquiry_type} from {self.name}"