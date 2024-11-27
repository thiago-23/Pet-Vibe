from django.db import models
from django.urls import reverse


class DogSize(models.Model):
    """
    Model to define different sizes of dogs for grooming services.
    """
    size = models.CharField(max_length=50, unique=True)
    duration = models.DurationField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.size} - ${self.price} - {self.duration}"


class GroomingService(models.Model):
    """
    Model to store grooming services offered.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    sizes = models.ManyToManyField(DogSize, related_name="services")
    image = models.ImageField(upload_to='service_images/', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('services')


class Testimonial(models.Model):
    """
    Model to store testimonials for grooming services.
    """
    name = models.CharField(max_length=100)
    service = models.ForeignKey(
        GroomingService, on_delete=models.CASCADE, related_name='testimonials'
    )
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Testimonial for {self.service} by {self.name}"

    def get_absolute_url(self):
        return reverse('testimonials')

    class Meta:
        ordering = ['created_on']