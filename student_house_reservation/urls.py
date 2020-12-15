# from django.urls import path
from django.urls import re_path, path

from student_house_reservation.views import EmployeeViewsUserList, EmployeeViewsAllUserReservationList, \
    EmployeeViewsSingleUserReservation, StudentViewsOwnReservationList, StudentAddReservationList, \
    StudentEditReservationList, TheCakeIsALie, EmployeeEditReservationList, EmployeeViewsStudentList

urlpatterns = [
    # HoneyPot urls
    path('___________________________________________/', TheCakeIsALie.as_view()),
    path('_____________^^_.-=_-=_-.^^________________/', TheCakeIsALie.as_view()),
    path('_________^^__(`-=_-=_-=_-`)_^^_____________/', TheCakeIsALie.as_view()),
    path('_^^________(`-=_-=_-=_-=_-=_`)_^^_^^_______/', TheCakeIsALie.as_view()),
    path('_____^^__(`-=_-=_-=_-=_-=_-=_-`)_^^_^^_____/', TheCakeIsALie.as_view()),
    path('________(`-=_-=_-=_-(_@)_-=_-=_-`)_____^^__/', TheCakeIsALie.as_view()),
    path('_______(`-=_-=_-=_-=_-=_-=_-=_-=`)_^^______/', TheCakeIsALie.as_view()),
    path('_______(`-=_-=_-=_-=_-=_-=_-=_-=`)_^^______/', TheCakeIsALie.as_view()),
    path('__^^___(`-=_-=_-=_-=_-=_-=_-=_-=`)______^^_/', TheCakeIsALie.as_view()),
    path('_______(`-=_-=_-=_-=_-=_-=_-=_-=`)_^^______/', TheCakeIsALie.as_view()),
    path('_______(`-=_-=_-=_-=_-=_-=_-=_-=`)_^^______/', TheCakeIsALie.as_view()),
    path('_______(`-=_-=_-=_-=_-=_-=_-=_-=`)_________/', TheCakeIsALie.as_view()),
    path('_______(`-=_-=_-=_-=_-=_-=_-=_-=`)_^^______/', TheCakeIsALie.as_view()),
    path('__^^____(`-=_-=_-=_-=_-=_-=_-=_`)_^^_______/', TheCakeIsALie.as_view()),
    path('_________(`-=_-=_-=_-=_-=_-=_-`)_^^__^^____/', TheCakeIsALie.as_view()),
    path('_____^^___(`-=_-=_-=_-=_-=_-`)_____________/', TheCakeIsALie.as_view()),
    path('______________`-=_-=_-=_-`________^^_______/', TheCakeIsALie.as_view()),
    path('___________________________________________/', TheCakeIsALie.as_view()),
    path('____---------HONEY_SWEET_HONEY---------____/', TheCakeIsALie.as_view()),
    path('-----------------I-LETS-GO-----------------/', TheCakeIsALie.as_view()),
    path('reservation/', TheCakeIsALie.as_view()),
    path('reservations/', TheCakeIsALie.as_view()),
    path('students-reservation/', TheCakeIsALie.as_view()),
    path('student-reservations/', TheCakeIsALie.as_view()),
    path('students/', TheCakeIsALie.as_view()),
    path('users/', TheCakeIsALie.as_view()),
    path('employees/', TheCakeIsALie.as_view()),
    path('student/', TheCakeIsALie.as_view()),
    path('user/', TheCakeIsALie.as_view()),
    path('employee/', TheCakeIsALie.as_view()),
    path('----------------DO-YOU-NOW----------------/', TheCakeIsALie.as_view()),
    path('____-----------POT_IS_EMPTY-----------____/', TheCakeIsALie.as_view()),
    path('__________________________________________/', TheCakeIsALie.as_view()),
    path('______________________%___________________/', TheCakeIsALie.as_view()),
    path('_____________________%%_%_________________/', TheCakeIsALie.as_view()),
    path('__``-.._.-``-.._.._-(||)(°)_______________/', TheCakeIsALie.as_view()),
    path('_____________________```__________________/', TheCakeIsALie.as_view()),
    path('__________________________________________/', TheCakeIsALie.as_view()),

    # Employee urls
    path('user-list/', EmployeeViewsUserList.as_view()),
    path('student-list/', EmployeeViewsStudentList.as_view()),
    re_path('reservation-list/user/(?P<user>\\d+)/', EmployeeViewsSingleUserReservation.as_view()),
    path('reservation-list/edit/<int:pk>/', EmployeeEditReservationList.as_view()),
    path('reservation-list/', EmployeeViewsAllUserReservationList.as_view()),

    # Student urls
    path('reservation-list/', StudentViewsOwnReservationList.as_view()),
    path('reservation-list/add/', StudentAddReservationList.as_view()),
    path('reservation-list/edit/<int:pk>/', StudentEditReservationList.as_view()),
]
