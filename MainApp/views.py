from django.shortcuts import render,redirect,HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import ServicesForm

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
            client_igst = request.POST.get('client_igst')
            client_sgst = request.POST.get('client_sgst')
            client_phone = request.POST.get('client_phone')
            client_email = request.POST.get('client_email')
            client_country = request.POST.get('client_country')
            client_state = request.POST.get('client_state')
            client_other_info = request.POST.get('client_other_info')

            provider_comp_name = request.POST.get('provider_comp_name')
            provider_name = request.POST.get('provider_name')
            provider_acc_no = request.POST.get('provider_acc_no')
            provider_bank_name = request.POST.get('provider_bank_name')
            provider_ifsc = request.POST.get('provider_ifsc')
            provider_gst = request.POST.get('provider_gst')
            provider_phone = request.POST.get('provider_phone')
            provider_mail = request.POST.get('provider_mail')
            provider_other_info = request.POST.get('provider_other_info')

            # Custom validations
            if len(client_comp_name) < 5 or len(provider_comp_name) < 5:
                raise ValueError('Client or Provider company name should contain at least 5 characters.')

            if len(client_email) < 12 or len(provider_mail) < 12:
                raise ValueError('Email should contain at least 12 characters.')

            if len(str(client_phone)) != 10 or len(provider_phone) != 10:
                raise ValueError('Phone No. should contain 10 digit.')

            if int(client_igst) < 0 or int(client_sgst) < 0 or (int(client_igst) + int(client_sgst)) > 18:
                raise ValueError('Invalid GST value.')

            if len(str(client_gst)) != 15 or len(str(provider_gst)) != 15:
                raise ValueError('GST Number should contain 15 digit.')

            # Additional email validation
            validate_email(client_email)
            validate_email(provider_mail)

            # Creating and saving the model object
            client_service_provider = ClientServiceProvider(
                client_comp_name=client_comp_name,
                client_gst=client_gst,
                client_igst=client_igst,
                client_sgst=client_sgst,
                client_phone=client_phone,
                client_email=client_email,
                client_country=client_country,
                client_state=client_state,
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

    try:
        all_client_provide = ClientServiceProvider.objects.all()[::-1]
    except ClientServiceProvider.DoesNotExist:
        all_client_provide = None

    context = {"all_client_provide": all_client_provide}

    return render(request, 'add_client.html', context)



def edit_client_provider(request, pk):
    obj_to_edit = get_object_or_404(ClientServiceProvider, pk=pk)
    
    if request.method == "POST":
        # Update the object with the posted data
        obj_to_edit.client_comp_name = request.POST.get('client_comp_name')
        obj_to_edit.client_gst = request.POST.get('client_gst')
        obj_to_edit.client_igst = request.POST.get('client_igst')
        obj_to_edit.client_sgst = request.POST.get('client_sgst')
        obj_to_edit.client_phone = request.POST.get('client_phone')
        obj_to_edit.client_email = request.POST.get('client_email')
        obj_to_edit.client_country = request.POST.get('client_country')
        obj_to_edit.client_state = request.POST.get('client_state')
        obj_to_edit.client_other_info = request.POST.get('client_other_info')
        
        obj_to_edit.provider_comp_name = request.POST.get('provider_comp_name')
        obj_to_edit.provider_name = request.POST.get('provider_name')
        obj_to_edit.provider_acc_no = request.POST.get('provider_acc_no')
        obj_to_edit.provider_bank_name = request.POST.get('provider_bank_name')
        obj_to_edit.provider_ifsc = request.POST.get('provider_ifsc')
        obj_to_edit.provider_gst = request.POST.get('provider_gst')
        obj_to_edit.provider_phone = request.POST.get('provider_phone')
        obj_to_edit.provider_mail = request.POST.get('provider_mail')
        obj_to_edit.provider_other_info = request.POST.get('provider_other_info')
        
        obj_to_edit.save()
        
        return redirect('add-client')  # Redirect to the desired URL after successful update
    
    return render(request, 'edit_client.html', {"obj_to_edit": obj_to_edit})
        

def delete_client_provider(request, pk):
    try:
        obj_to_delete = get_object_or_404(ClientServiceProvider, pk=pk)
        obj_to_delete.delete()
        messages.success(request, 'Record deleted successfully !')
        return redirect('/add-client/')
    except:
        messages.error(request, 'Record not deleted !')
        return redirect('/add-client/')
    

def assigne_services(request):
    if request.method == 'POST':
        form = ServicesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/assigne-client-services/')
    else:
        form = ServicesForm()

    return render(request, 'services.html',  {'form': form})


def create_services(request):
    if request.method == 'POST':
        form = ServicesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Services successfully assigned.')
            # return redirect('/assigne-client-services/')

    return render(request, 'services_form.html', {'form':ServicesForm()})

