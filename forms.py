from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
import datetime

class RoomForm(forms.ModelForm):
    roomfacility = forms.ModelMultipleChoiceField(queryset=Facilities.objects, widget=forms.CheckboxSelectMultiple())

class DateInput(forms.DateInput):
    input_type = 'date'
    
class AddBooking(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ['name','mobile_no','id_type','gender','address','checkin_date','checkout_date']
        widgets = {
            'checkin_date': DateInput(),
            'checkout_date': DateInput(),
            'gender': forms.RadioSelect()
        }

    # def __init__(self, *args, **kwargs):
    #     super(AddBooking, self).__init__(*args, **kwargs)
    #     self.fields['checkin_date'].widget.attrs\
    #         .update({
    #             'id': 'checkin'
    #         })
    #     self.fields['checkout_date'].widget.attrs\
    #     .update({
    #         'id': 'checkout'
    #     })

class UpdateBooking(AddBooking):

    class Meta:
        model = Booking
        fields = ['name','mobile_no','id_type','gender','address','checkin_date','checkout_date','roomid']
        widgets = {
            'checkin_date': DateInput(),
            'checkout_date': DateInput(),
            'gender': forms.RadioSelect()
        }
        labels = {
            'roomid': ('Room Type')
        }

class Contact(forms.ModelForm):

    class Meta:
        model = Enquiry
        fields = ['name','email','query_msg']
        widgets = {
            'query_msg': forms.Textarea()
        }
        labels = {
            'name': ('Your Name'),
            'email': ('Your email'),
            'query_msg': ('Query Message')
        }
