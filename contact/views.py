from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.views import generic, View
from django.views.generic import DeleteView
from django.conf import settings
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from .forms import ContactForm
from .models import Contact


class ContactUs(View):
    """
    Handles displaying and processing the contact form.
    """
    def get(self, request):
        """
        Renders the contact form.
        """
        form = ContactForm()
        return render(request, "contact/contact.html", {"contact_form": form})

    def post(self, request):
        """
        Handles contact form submissions.
        """
        form = ContactForm(data=request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()

            # Prepare confirmation email
            subject = render_to_string(
                'contact/confirmation_emails/confirmation_email_subject.txt',
                {'subject': contact.enquiry_type}
            )
            message = render_to_string(
                'contact/confirmation_emails/confirmation_email_body.txt',
                {'name': contact.name, 'subject': contact.enquiry_type}
            )

            # Send confirmation email
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [contact.email],
            )
            messages.success(request, "Your enquiry has been submitted successfully!")
            return redirect("home")
        else:
            messages.error(request, "There was an error submitting the form. Please try again.")
        return render(request, "contact/contact.html", {"contact_form": form})

class EnquiriesListView(generic.ListView):
    """
    Displays a list of all enquiries for admin.
    """
    model = Contact
    template_name = "contact/enquiries_dashboard.html"
    context_object_name = "enquiries"

    def get_queryset(self):
        return Contact.objects.all().order_by("-date")


class EnquiryDetailView(generic.DetailView):
    """
    Displays details of a specific enquiry.
    """
    model = Contact
    template_name = "contact/enquiry_detail.html"
    context_object_name = "enquiry"


class DeleteEnquiryView(DeleteView):
    """
    This view allows admin to delete an enquiry.
    """
    model = Contact
    template_name = "contact/delete_enquiry.html"
    success_url = reverse_lazy('enquiries')

    def delete(self, request, *args, **kwargs):
        """
        Override delete to add a success message.
        """
        messages.success(request, "Enquiry deleted successfully!")
        return super().delete(request, *args, **kwargs)