from django.contrib import admin

# Register your models here.
from student_house_reservation.models import Reservation

admin.site.register(Reservation)