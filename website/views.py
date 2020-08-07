from django.shortcuts import render
from website.models import Contact
from website.models import Appointment


# Create your views here.
def home(request):
    return render(request,'home.html',{})
def contact(request):
    if request.method == "POST":
        message_name=request.POST.get('message-name')
        message_email=request.POST.get('message-email')
        message=request.POST.get('message')
        contact=Contact(name=message_name,email=message_email,message=message)
        contact.save()
        
       
        return render(request,'contact.html',{'message-name':message_name})

    else:
        return render(request,'contact.html',{})

def about(request):
    return render(request,'about.html',{})

def service(request):
    return render(request,'service.html',{})


def pricing(request):
    return render(request,'pricing.html',{})
def appointment(request):
    if request.method == "POST":
        your_name=request.POST.get('your-name')
        your_phone=request.POST.get('your-phone')
        your_email=request.POST.get('your-email')
        your_address=request.POST.get('your-address')
        your_scheldule=request.POST.get('your-scheldule')
        your_date=request.POST.get('your-date')
        your_message=request.POST.get('your-message')
        
        appointment = Appointment(name=your_name,email=your_email,message=your_message,phone=your_phone,date=your_date,adderss=your_address,first_choice_appointment=your_scheldule)
        appointment.save()
        

        
        return render(request,'appointment.html',{'your_scheldule':your_scheldule,'your_name':your_name,'your_phone':your_phone,'your_email':your_email,'your_address':your_address,'your_date':your_date})

    else:
        return render(request,'home.html',{})
