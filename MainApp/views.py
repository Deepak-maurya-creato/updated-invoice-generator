from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Handle invalid login
            messages.error(request, 'Invalid credentials!')
            return redirect('login')  # Redirect back to login page

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'dashboard.html')


@login_required
def add_client(request):
    if request.method == 'POST':
        try:
            client_comp_name = request.POST.get('client_comp_name')
            client_gst = request.POST.get('client_gst')
            client_phone = request.POST.get('client_phone')
            client_email = request.POST.get('client_email')
            client_country = request.POST.get('client_country')
            client_state = request.POST.get('client_state')
            client_pin = request.POST.get('client_pin')
            client_other_info = request.POST.get('client_other_info')

            provider_comp_name = request.POST.get('provider_comp_name')
            provider_name = request.POST.get('provider_name')
            provider_acc_no = request.POST.get('provider_acc_no')
            provider_bank_name = request.POST.get('provider_bank_name')
            provider_ifsc = request.POST.get('provider_ifsc')
            provider_gst = request.POST.get('provider_gst')
            provider_phone = request.POST.get('provider_phone')
            provider_mail = request.POST.get('provider_mail')
            provider_other_info  = request.POST.get('provider_other_info')

            # Custom validations
            if len(client_comp_name) < 5 or len(provider_comp_name) < 5:
                raise ValueError('Client or Provider company name should contain at least 5 characters.')

            if len(client_email) < 12 or len(provider_mail) < 12:
                raise ValueError('Email should contain at least 12 characters.')

            if len(str(client_phone)) != 10 or len(provider_phone) != 10:
                raise ValueError('Phone No. should contain 10 digit.')
            
            if len(str(client_pin)) != 6:
                raise ValueError('Zip Code should contain 6 digit.')
            
            if len(str(client_gst)) != 15 or len(str(provider_gst)) != 15:
                raise ValueError('GST Number should contain 15 digit.')

            # Additional email validation
            validate_email(client_email)
            validate_email(provider_mail)

            # Creating and saving the model object
            client_service_provider = ClientServiceProvider(
                client_comp_name=client_comp_name,
                client_gst=client_gst,
                client_phone=client_phone,
                client_email=client_email,
                client_country=client_country,
                client_state=client_state,
                client_pin=client_pin,
                client_other_info=client_other_info,
                provider_comp_name=provider_comp_name,
                provider_name=provider_name,
                provider_acc_no=provider_acc_no,
                provider_bank_name=provider_bank_name,
                provider_ifsc=provider_ifsc,
                provider_gst=provider_gst,
                provider_phone=provider_phone,
                provider_mail=provider_mail,
                provider_other_info=provider_other_info
            )
            client_service_provider.save()

            messages.success(request, 'Data saved successfully.')

        except ValidationError as e:
            messages.error(request, f'Email validation error: {e}')

        except ValueError as e:
            messages.error(request, f'Validation error: {e}')
            
        except Exception as e:
            messages.error(request, f'Error occurred: {str(e)}')

    return render(request, 'add_client.html')
