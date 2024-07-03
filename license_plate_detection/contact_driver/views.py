from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import SignUpForm, RegistrationForm, SearchForm
from django.contrib.auth import authenticate, login, logout
from .models import Registration
from django.http import JsonResponse
from .license_plate_detection import detect_license_plate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def home(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    return render(request, "contact_driver/home.html")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password != confirm_password:
                messages.error(request, "Passwords do not match")
                return redirect('signup')
            myuser = User.objects.create_user(username=email, email=email, password=password)
            messages.success(request, "Your account has been successfully created")
            return redirect('signin')
    else:
        form = SignUpForm()
    return render(request, "contact_driver/signup.html", {'form': form})

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully signed in.")
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password. Please try again.")
    return render(request, "contact_driver/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Succesfully")
    return redirect('signin')

def contact_us(request):
    return render(request, 'contact_driver/contact_us.html')

def products(request):
    return render(request, 'contact_driver/products.html')

def testimonials(request):
    return render(request, 'contact_driver/testimonials.html')

def about_us(request):
    return render(request, 'contact_driver/about_us.html')

def success_page(request):
    return render(request, 'contact_driver/success_page.html')

def registration_form(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.username = form.cleaned_data['username']
            registration.roll_number = form.cleaned_data['roll_number']
            registration.license_plate_number = form.cleaned_data['license_plate_number']
            registration.email = form.cleaned_data['email']
            registration.phone_number = form.cleaned_data['phone_number']
            registration.contact_method = form.cleaned_data['contact_method']
            registration.visibility = request.POST.get('visibility') == 'on'
            registration.save()
            messages.success(request, 'You have been successfully registered!')
            return redirect('success_page')
    else:
        form = RegistrationForm()
    return render(request, 'contact_driver/registration_form.html', {'form': form})


def search_page(request):
    form = SearchForm()
    return render(request, 'contact_driver/search_page.html', {'form': form})

def search_results(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            license_plate_number = form.cleaned_data['license_plate_number']
            results = Registration.objects.filter(license_plate_number__icontains=license_plate_number)
            return render(request, 'contact_driver/search_results.html', {'results': results})
    return redirect('search_page')

def open_camera_view(request):
    if request.method == 'GET':
        detected_text = detect_license_plate()
        return JsonResponse({'detected_text': detected_text})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
