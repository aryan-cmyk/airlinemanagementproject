from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .models import UserProfile
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            try:
                profile = UserProfile.objects.get(user=user)
                role = profile.title.lower()
            except UserProfile.DoesNotExist:
                return JsonResponse({'error': 'No profile found for this user.'})

            if role == 'crew':
                return JsonResponse({'message': 'Login successful!', 'redirect_url': '/crew/'})
            elif role == 'employee':
                return JsonResponse({'message': 'Login successful!', 'redirect_url': '/home/'})
            else:
                return JsonResponse({'message': 'Login successful!', 'redirect_url': '/booking/'})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)

    return render(request, 'loginpage.html')

# Pages / Views
def home_view(request):
    return render(request, 'homepage.html')

def user_view(request):
    return render(request, 'user.html')

def new_flight_view(request):
    return render(request, 'newflight.html')

def manage_flights_view(request):
    return render(request, 'manageflights.html')

def airbus_view(request):
    return render(request, 'newairbus.html')

def accounts_view(request):
    return render(request, 'accounts.html')

def crew_view(request):
    return render(request, 'crew.html')

def assign_crew_view(request):
    return render(request, 'assigncrew.html')

def view_schedule_view(request):
    return render(request, 'viewschedule.html')

def booking_view(request):
    return render(request, 'booking.html')

def my_bookings_view(request):
    return render(request, 'mybookings.html')

def logout_view(request):
    logout(request)
    return redirect('login') 

def create_account_view(request):
    return render(request, 'accounts.html')

def password_reset_view(request):
    return render(request, 'passwordreset.html')    