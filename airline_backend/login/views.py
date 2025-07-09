from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import UserProfile
import json

def custom_login_view(request):
    if request.method == "GET":
        return render(request, "loginpage.html")

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")

            if not username or not password:
                return JsonResponse({"error": "Username and password are required"}, status=400)

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)

                try:
                    profile = UserProfile.objects.get(user=user)
                    title = profile.title
                except UserProfile.DoesNotExist:
                    title = "Unknown"

                return JsonResponse({
                    "message": "Login successful!",
                    "title": title,
                    "username": user.username
                }, status=200)
            else:
                return JsonResponse({"error": "Invalid username or password"}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)
