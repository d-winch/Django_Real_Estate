from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
import os

is_prod = os.environ.get('IS_HEROKU', None)

if is_prod:
    # Get var from Heroku config vars
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
else:
    from djp.local_settings import EMAIL_HOST_USER

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if user has salready sent an inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('listing', listing_id=listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,
        phone=phone, message=message, user_id=user_id)

        contact.save()

        # Send email
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info.',
            EMAIL_HOST_USER,
            [EMAIL_HOST_USER],  # , realtor_email], # Send to own email as a test, as realtor emails are not real
            fail_silently=False
        )

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
        return redirect('listing', listing_id=listing_id)
