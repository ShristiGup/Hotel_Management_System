from django.contrib import admin
from .models import *
from .forms import *

class BookingAdmin(admin.ModelAdmin):
    list_display = ("roomid", "booked_by_user","name","mobile_no","booking_no")
    list_filter = ("status",)
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["roomid", "booked_by_user","name","mobile_no","booking_no","id_type","gender","address","checkin_date","checkout_date","booking_date"]
        else:
            return []

    def has_add_permission(self, request):
        return False

class RoomAdmin(admin.ModelAdmin):
    form = RoomForm


admin.site.register(Category)
admin.site.register(Facilities)
admin.site.register(Enquiry)
admin.site.register(Room, RoomAdmin)
admin.site.register(Booking, BookingAdmin)

