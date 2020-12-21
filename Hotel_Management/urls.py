"""Hotel_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hotel.models import *
from hotel import views as hotel_views
from users import views as users_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

category = Category.objects.all()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',hotel_views.index,name='index'),
    path('room/<str:roomtype>/',hotel_views.room_details,name='room-details'),
    path('facilities/',hotel_views.facilities,name='facilities'),
    path('gallery/',hotel_views.gallery,name='gallery'),
    path('about-us/',hotel_views.about_us,name='about-us'),
    path('register/',users_views.register,name='register'),
    path('user/profile/',users_views.profile,name='profile'),
    path('contact/',hotel_views.CreateEnquiry.as_view(),name='contact'),
    path('view-messages/<str:username>/',hotel_views.ListMessages.as_view(),name='list-messages'),
    path('booking/new/<int:id>/',hotel_views.CreateBooking.as_view(),name='create-booking'),
    path('bookings/<str:username>/',hotel_views.ListBooking.as_view(),name='list-booking'),
    path('booking/<int:pk>/',hotel_views.DetailedBooking.as_view(),name='booking-detail'),
    path('booking/<int:pk>/update',hotel_views.UpdateBooking.as_view(),name='booking-update'),
    path('booking/<int:pk>/delete',hotel_views.DeleteBooking.as_view(),name='booking-delete'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html',extra_context={'category':category}),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html',extra_context={'category':category}),name='logout'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html',extra_context={'category':category}),name='password_reset'),
    path('password-reset-done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
