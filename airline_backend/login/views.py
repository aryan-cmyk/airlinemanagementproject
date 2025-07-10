from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .models import UserProfile
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import UserProfile

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


def accounts_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        title = request.POST['title']

        user = User.objects.create(username=username, email=email, password=password)
        UserProfile.objects.create(user=user, title=title)

        return redirect('accounts')  # Redirect to same page to refresh list

    # Fetch all existing user profiles
    accounts = UserProfile.objects.select_related('user').all()
    return render(request, 'accounts.html', {'accounts': accounts})


# Password reset view
def password_reset_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        new_password = request.POST['new_password']

        try:
            user = User.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            return redirect('login')
        except User.DoesNotExist:
            return render(request, 'passwordreset.html', {'error': 'User not found.'})

    return render(request, 'passwordreset.html')


def delete_account(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('accounts')

def edit_account(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    profile = get_object_or_404(UserProfile, user=user)

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        title = request.POST.get('title')
        password = request.POST.get('password', '')  # ✅ Safe access

        user.username = username
        user.email = email
        if password.strip():  # ✅ Update only if not empty
            user.set_password(password)
        user.save()

        profile.title = title
        profile.save()

        return redirect('accounts')

    return render(request, 'edit_account.html', {
        'user_obj': user,
        'profile': profile,
    })
