from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User


def Register_User(request):

    if request.method == 'POST':
        # Get the form data
        username = request.POST.get('username')
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Manual validation
        errors = []

        # Validate username
        if User.objects.filter(username=username).exists():
            errors.append("Username already taken.")

        if User.objects.filter(email=email).exists():
            errors.append("Email already in use.")

        # Validate passwords
        if password != confirm_password:
            errors.append("Passwords do not match.")

        if errors:
            # If there are errors, show them as messages
            for error in errors:
                messages.error(request, error)
        else:
            # Create user if no errors
            user = User.objects.create_user(
                username=username,
                first_name=fname,
                last_name=lname,
                email=email,
                password=password
                )
            # create api key
            
           
            messages.success(request, "Account created successfully!")
            # Authenticate and log the user in
            login(request, user)
            
            
            return redirect('home')  # Redirect to home or desired page

    return render(request, 'register.html')

def Login_User(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successfully !")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials!")
    return render(request, 'login.html')

def Logout_User(request):
    logout(request)
    
    messages.success(request, "Logout Successfully !")
    return redirect('login')

