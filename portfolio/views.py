from django.shortcuts import render,redirect

# Create your views here.

def Home(request):
    return render(request,'portfolio/index.html')



def About(request):
    return render(request,'portfolio/about.html')


def Contact(request):
    return render(request,'portfolio/contact.html')


def Resource(request):
    return render(request,'portfolio/article.html')

# views.py
# views.py
# views.py
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .forms import ContactForm

def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()  # Save form data to get instance
            send_contact_email(contact_message)
            return redirect('contact_success')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})

def send_contact_email(contact_message):
    subject = 'Regarding Contact'
    html_message = render_to_string('email/contact_email.html', {'contact_message': contact_message})
    plain_message = strip_tags(html_message)  # Strip HTML tags for plain text version

    from_email = settings.EMAIL_HOST_USER
    to_email_user = [contact_message.email]  # Send email to the user who filled the form
    to_email_owner = [settings.EMAIL_HOST_USER]  # Send email to the website owner

    # Create email with both HTML and plain text content
    email = EmailMultiAlternatives(subject, plain_message, from_email, to_email_user)
    email.attach_alternative(html_message, "text/html")  # Attach HTML content as alternative
    email.send()

    # Also send email to the website owner
    email_owner = EmailMultiAlternatives(subject, plain_message, from_email, to_email_owner)
    email_owner.attach_alternative(html_message, "text/html")  # Attach HTML content as alternative
    email_owner.send()

def contact_success_view(request):
    return render(request, 'email/success_mail.html')
