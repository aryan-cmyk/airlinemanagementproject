from django.urls import path
from . import views
from .views import (
    login_view,
    home_view,
    crew_view,
    assign_crew_view,
    booking_view,
    user_view,
    new_flight_view,
    manage_flights_view,
    airbus_view,
    accounts_view,
    view_schedule_view,
    my_bookings_view,
    logout_view,
    create_account_view,   # ✅ Add this line
    password_reset_view  
)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('crew/', crew_view, name='crew'),
    path('assign_crew/', assign_crew_view, name='assign_crew'),
    path('booking/', booking_view, name='booking'),
    path('mybookings/', my_bookings_view, name='mybookings'),  # ✅ THIS LINE

    # Additional routes
    path('user/', user_view, name='user'),
    path('newflight/', new_flight_view, name='newflight'),
    path('manageflights/', manage_flights_view, name='manageflights'),
    path('newairbus/', airbus_view, name='newairbus'),
    path('accounts/', accounts_view, name='accounts'),
    path('viewschedule/', view_schedule_view, name='view_schedule'),
    path('logout/', logout_view, name='logout'),
    path('createaccount/', create_account_view, name='createaccount'),
    path('passwordreset/', password_reset_view, name='passwordreset'),
    path('accounts/delete/<int:user_id>/', views.delete_account, name='delete_account'),
    path('accounts/edit/<int:user_id>/', views.edit_account, name='edit_account'),
]




