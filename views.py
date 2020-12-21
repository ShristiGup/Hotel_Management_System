from django.shortcuts import render
from .models import *
from .forms import *
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from users.models import CustomUser
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from django.shortcuts import get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.

def index(request):
    category = Category.objects.all()
    facility = Facilities.objects.all().order_by("-id")[:4]
    context = {'category':category,'facility':facility}
    return render(request,'hotel/home.html',context)

def room_details(request,roomtype):
    category = Category.objects.all()
    catgry = Category.objects.get(categoryname = roomtype)
    room = Room.objects.get(roomtype=catgry)
    context = {'category':category,'room':room}
    return render(request,'hotel/room_details.html',context)

def facilities(request):
    category = Category.objects.all()
    facility = Facilities.objects.all()
    context = {'category':category,'facility':facility}
    return render(request,'hotel/facilities.html',context)

def gallery(request):
    category = Category.objects.all()
    room = Room.objects.all()
    context = {'category':category,'room':room}
    return render(request,'hotel/gallery.html',context)

def about_us(request):
    category = Category.objects.all()
    context = {'category':category}
    return render(request,'hotel/about_us.html',context)

class CreateBooking(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Booking
    form_class = AddBooking
    success_message = "Yayy!You have a new booking created with BookingID: %(booking_no)s"

    def get_success_url(self):
        return reverse('list-booking',args = [self.request.user])

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            booking_no=self.object.booking_no,
        )

    def form_valid(self,form):
        form.instance.booked_by_user = self.request.user
        form.instance.roomid = Room.objects.get(id = self.kwargs['id'])
        return super().form_valid(form)
    
    def get_context_data(self, *args, **kwargs):
        context = super(CreateBooking, self).get_context_data(*args, **kwargs)
        context['category'] = Category.objects.all()
        return context

class ListBooking(LoginRequiredMixin,ListView):
    model = Booking
    context_object_name = "bookings"
    template_name = "hotel/my_booking.html"
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(CustomUser,username = self.kwargs.get('username'))
        return Booking.objects.filter(booked_by_user=user).order_by("-booking_date")

    def get_context_data(self, *args, **kwargs):
        context = super(ListBooking, self).get_context_data(*args, **kwargs)
        context['category'] = Category.objects.all()
        return context
        
class DetailedBooking(LoginRequiredMixin,DetailView):
    model = Booking

    def get_context_data(self, *args, **kwargs):
        context = super(DetailedBooking, self).get_context_data(*args, **kwargs)
        context['category'] = Category.objects.all()
        return context

class UpdateBooking(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Booking
    form_class = UpdateBooking
    success_message = "Yayy!Your booking is updated..."

    def form_valid(self,form):
        form.instance.booked_by_user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, *args, **kwargs):
        context = super(UpdateBooking, self).get_context_data(*args, **kwargs)
        context['category'] = Category.objects.all()
        return context

class DeleteBooking(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Booking
    success_message = "Your booking is deleted!"

    def get_success_url(self):
        return reverse('list-booking',args = [self.request.user])
    
    def get_context_data(self, *args, **kwargs):
        context = super(DeleteBooking, self).get_context_data(*args, **kwargs)
        context['category'] = Category.objects.all()
        return context
    
    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(DeleteBooking, self).delete(request, *args, **kwargs)
    
class CreateEnquiry(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Enquiry
    form_class = Contact
    success_url = reverse_lazy('contact')
    success_message = "Yayy!Your query has been forwarded to the Admin..."

    def form_valid(self,form):
        form.instance.enquired_by = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, *args, **kwargs):
        context = super(CreateEnquiry, self).get_context_data(*args, **kwargs)
        context['category'] = Category.objects.all()
        return context

class ListMessages(LoginRequiredMixin,ListView):
    model = Enquiry
    context_object_name = "enquiries"
    template_name = "hotel/messages.html"
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(CustomUser,username = self.kwargs.get('username'))
        return Enquiry.objects.filter(enquired_by=user).order_by("-id")

    def get_context_data(self, *args, **kwargs):
        context = super(ListMessages, self).get_context_data(*args, **kwargs)
        context['category'] = Category.objects.all()
        return context