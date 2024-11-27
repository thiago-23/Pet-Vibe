from django.contrib import admin
from .models import DogSize, GroomingService, Testimonial


@admin.register(DogSize)
class DogSizeAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing Dog Sizes.
    """
    list_display = ('size', 'price', 'duration')
   


@admin.register(GroomingService)
class GroomingServiceAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing Grooming Services.
    """
    list_display = ('name', 'description')
    


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing Testimonials.
    """
    list_display = ('name', 'service', 'is_approved', 'created_on')
    list_filter = ('is_approved', 'created_on')
    search_fields = ('name', 'service')
    actions = ['approve_testimonials']

    def approve_testimonials(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(request, "Selected testimonials have been approved.")
