# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.exceptions import APIException

from student_house_reservation.models import Reservation
from student_house_reservation.serializers import ReservationSerializer, EmployeeReservationListSerializer, \
    StudentReservationSerializer, EmployeeStudentListSerializer

from student_house_reservation.permissions import IsTheCake, IsEmployee, IsStudent
from student_house_reservation.serializers import EmployeeUserListSerializer, StudentAddReservationSerializer, \
    StudentEditReservationSerializer


# Honeypot view: Cracker has been hacked
class TheCakeIsALie(generics.ListAPIView):
    permission_classes = [IsTheCake]
    serializer_class = ReservationSerializer


# Employee views
class EmployeeViewsUserList(generics.ListAPIView):
    permission_classes = [IsEmployee]
    serializer_class = EmployeeUserListSerializer

    def get_queryset(self):
        return get_user_model().objects.filter(is_superuser=False)


# Employee views
class EmployeeViewsStudentList(generics.ListAPIView):
    permission_classes = [IsEmployee]
    serializer_class = EmployeeStudentListSerializer

    def get_queryset(self):
        return get_user_model().objects.filter(is_superuser=False).exclude(groups__name='Employee')


class EmployeeViewsAllUserReservationList(generics.ListAPIView):
    permission_classes = [IsEmployee]
    queryset = Reservation.objects.all()
    serializer_class = EmployeeReservationListSerializer


# Student views
class StudentViewsOwnReservationList(generics.ListAPIView):
    permission_classes = [IsStudent]
    serializer_class = StudentReservationSerializer

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)


class StudentAddReservationList(generics.CreateAPIView):
    permission_classes = [IsStudent]
    serializer_class = StudentAddReservationSerializer

    def perform_create(self, serializer):
        if Reservation.objects.filter(user=self.request.user).count() >= 1:
            raise APIException('Kind student, you can only own 1 reservation, please edit yours')
        serializer.save(user=self.request.user)


class StudentEditReservationList(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsStudent]
    queryset = Reservation.objects.all()
    serializer_class = StudentEditReservationSerializer
