from django.contrib.auth import get_user_model
from rest_framework import serializers

from student_house_reservation.models import Reservation


# Honeypot for the bees
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ()
        model = Reservation


# List of all reservation for the Employee
class EmployeeReservationListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'neighborhood', 'room_type', 'user')
        model = Reservation


# List of all user for the Employee
class EmployeeUserListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username', 'email', 'is_staff', 'groups')
        model = get_user_model()

# List of all student for the Employee
class EmployeeStudentListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username', 'email')
        model = get_user_model()


# Show reservation of the current student (user)
class StudentReservationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'neighborhood', 'room_type', 'user')
        model = Reservation


# Show reservation of the current student (user)
class StudentAddReservationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'neighborhood', 'room_type')
        model = Reservation


# Edit reservation of the current student (user)
class StudentEditReservationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'neighborhood', 'room_type')
        model = Reservation
