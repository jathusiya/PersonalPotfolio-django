from django.shortcuts import render
from django.http import HttpResponse
from  django.contrib import messages
from Base import models
from django.core.mail import send_mail
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def home(request):
    return render(request,'home.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        content = request.POST.get('content')

        if 2 <= len(name) <= 30:
            pass
        else:
            messages.error(request, 'Length of name should be between 2 and 30 characters')
            return render(request, 'home.html')

        if 2 <= len(email) <= 30:
            pass
        else:
            messages.error(request, 'Invalid email, please try again')
            return render(request, 'home.html')

        if 10 <= len(phone) <= 13:
            pass
        else:
            messages.error(request, 'Invalid phone number, please try again')
            return render(request, 'home.html')

        # Save data to the model
        ins = models.Contact(name=name, phone=phone, email=email, subject=subject, content=content)
        ins.save()

        # Send confirmation email
        sub = "This is an automatically generated message"
        msg = "Thank you for contacting me. I will get back to you soon!!!"
        send_mail(sub, msg, settings.DEFAULT_FROM_EMAIL, [email], fail_silently=False,)
    
        messages.success(request, 'Thank you for connecting with me')

    return render(request, 'home.html')

