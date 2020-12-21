from django.db import models
from django import forms
from users.models import CustomUser
from random import randint
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    categoryname = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.categoryname

    class Meta:
        verbose_name_plural = 'Categories'

class Facilities(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(default='fac.jpg',upload_to='fac_pics')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Facilities'

class Room(models.Model):
    roomtype = models.ForeignKey(Category,on_delete=models.CASCADE)
    roomname = models.CharField(max_length=100)
    maxadult = models.IntegerField()
    maxchild = models.IntegerField()
    roomdesc = models.TextField()
    no_of_bed = models.IntegerField()
    image = models.ImageField(default='room.jpg',upload_to='room_pics')
    roomfacility = models.ManyToManyField(Facilities)

    def __str__(self):
        return self.roomname

ID_TYPE = (
    ('Aadhaar Card','Aadhaar Card'),
    ('PAN Card','PAN Card'),
    ('Voter ID','Voter ID'),
    ('Passport','Passport'),
    ('Driving License','Driving License'),
)

GENDER = [
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other'),
]

STATUS = (
    ('Accepted','Accepted'),
    ('Rejected','Rejected'),
    ('Pending','Pending'),
)

def booking_no_generator():
    return str(randint(10000000000, 99999999999))

def validate_date(d):
        if d < timezone.now().date():
            raise forms.ValidationError('Date cannot be in the past')
        
class Booking(models.Model):
    roomid = models.ForeignKey(Room,on_delete=models.CASCADE)
    booked_by_user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    mobile_no = models.CharField(max_length=10)
    booking_no = models.CharField(max_length=20,default = booking_no_generator)
    id_type = models.CharField(max_length=25, choices=ID_TYPE, default='Aadhaar Card')
    gender = models.CharField(max_length=10,choices=GENDER,default='Male')
    address = models.TextField()
    checkin_date = models.DateField(validators=[validate_date])
    checkout_date = models.DateField(validators=[validate_date])
    booking_date = models.DateTimeField(auto_now_add=True)
    remark = models.TextField(null=True)
    status = models.CharField(max_length=20,choices=STATUS, default='Pending')

    def __str__(self):
        return self.booking_no

    def get_absolute_url(self):
        return reverse('booking-detail',kwargs={'pk':self.pk})

class Enquiry(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    enquired_by = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    query_msg = models.TextField()
    query_response = models.TextField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Enquiries'