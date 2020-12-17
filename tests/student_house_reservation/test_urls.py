import json

import pytest
from django.contrib.auth.models import Group, Permission, User
from mixer.backend.django import mixer
from rest_framework.status import *
from rest_framework.test import APIClient


@pytest.fixture()
def student_house_reservation(db):
    return [
        mixer.blend('student_house_reservation.Reservation') for _ in range(3)
    ]


@pytest.fixture()
def groupStudent(db):
    group = Group(name='Student')
    group.save()
    perm1 = Permission.objects.get(name='Can view reservation')
    perm2 = Permission.objects.get(name='Can change reservation')
    perm3 = Permission.objects.get(name='Can add reservation')
    group.permissions.add(perm1)
    group.permissions.add(perm2)
    group.permissions.add(perm3)
    return group


@pytest.fixture()
def groupEmployee(db):
    group = Group(name='Employee')
    group.save()
    group.permissions.add(Permission.objects.get(name='Can view reservation'))
    return group


def get_client(user=None):
    res = APIClient()
    if user is not None:
        res.force_login(user)
    return res


def parse(response):
    response.render()
    content = response.content.decode()
    return json.loads(content)


def contains(response, key, value):
    obj = parse(response)
    if key not in obj:
        return False
    return value in obj[key]


########ACCESS_TO_HONEYPOT########

############# THE CAKE IS A LIE VIEW ######################
def test_reservations_anon_user_get_nothing_from_cake_is_a_lie_view():
    path = '/api/v1/reservation/'
    client = get_client()
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'credentials were not provided')


def test_reservations_student_user_get_nothing_from_cake_is_a_lie_view(groupStudent):
    path = '/api/v1/reservation/'
    student_test = mixer.blend(User)
    student_test.groups.add(groupStudent)
    student_test.save()
    client = get_client(student_test)
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'You do not have permission to perform this action.')


def test_reservations_employee_user_get_nothing_from_cake_is_a_lie_view(groupEmployee):
    path = '/api/v1/reservation/'
    employee_test = mixer.blend(User)
    employee_test.groups.add(groupEmployee)
    employee_test.save()
    client = get_client(employee_test)
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'You do not have permission to perform this action.')

######################################################################################
################# FROM EmployeeViewsUserList VIEW####################################
def test_reservations_anon_user_get_nothing_from_EmployeeViewsUserList_view():
    path = '/api/v1/user-list/'
    client = get_client()
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'credentials were not provided')


def test_reservations_student_user_get_nothing_from_EmployeeViewsUserList_view(groupStudent):
    path = '/api/v1/user-list/'
    student_test = mixer.blend(User)
    student_test.groups.add(groupStudent)
    student_test.save()
    client = get_client(student_test)
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'You do not have permission to perform this action.')


def test_reservations_employee_user_get_nothing_from_EmployeeViewsUserList_view(groupEmployee):
    path = '/api/v1/user-list/'
    employee_test = mixer.blend(User)
    employee_test.groups.add(groupEmployee)
    employee_test.save()
    client = get_client(employee_test)
    response = client.get(path)
    assert response.status_code == HTTP_200_OK


######################################################################################
##########################ACCESS TO EmployeeViewsStudentList VIEW##################à

def test_reservations_anon_user_get_nothing_from_EmployeeViewsStudentList_View():
    path = '/api/v1/student-list/'
    client = get_client()
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'credentials were not provided')


def test_reservations_student_user_get_nothing_from_EmployeeViewsStudentList_View(groupStudent):
    path = '/api/v1/student-list/'
    student_test = mixer.blend(User)
    student_test.groups.add(groupStudent)
    student_test.save()
    client = get_client(student_test)
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'You do not have permission to perform this action.')


def test_reservations_employee_user_get_nothing_from_EmployeeViewsStudentList_View(groupEmployee):
    path = '/api/v1/student-list/'
    employee_test = mixer.blend(User)
    employee_test.groups.add(groupEmployee)
    employee_test.save()
    client = get_client(employee_test)
    response = client.get(path)
    assert response.status_code == HTTP_200_OK


######################################################################################
######################### EmployeeViewsAllUserReservationList ########################

def test_reservations_anon_user_get_nothing_from_EmployeeViewsAllUserReservationList_view():
    path = '/api/v1/reservation-list/'
    client = get_client()
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'credentials were not provided')


def test_reservations_student_user_get_nothing_from_EmployeeViewsAllUserReservationList_view(groupStudent):
    path = '/api/v1/reservation-list/'
    student_test = mixer.blend(User)
    student_test.groups.add(groupStudent)
    student_test.save()
    client = get_client(student_test)
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'You do not have permission to perform this action.')


def test_reservations_employee_user_get_nothing_from_EmployeeViewsAllUserReservationList_view(groupEmployee):
    path = '/api/v1/reservation-list/'
    employee_test = mixer.blend(User)
    employee_test.groups.add(groupEmployee)
    employee_test.save()
    client = get_client(employee_test)
    response = client.get(path)
    assert response.status_code == HTTP_200_OK


######################################################################################
########################### StudentViewsOwnReservationList ###########################
def test_reservations_anon_user_get_nothing_from_StudentViewsOwnReservationList_view():
    path = '/api/v1/reservation-student/'
    client = get_client()
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'credentials were not provided')


def test_reservations_student_user_get_nothing_from_StudentViewsOwnReservationList_view(groupStudent):
    path = '/api/v1/reservation-student/'
    student_test = mixer.blend(User)
    student_test.groups.add(groupStudent)
    student_test.save()
    client = get_client(student_test)
    response = client.get(path)
    assert response.status_code == HTTP_200_OK


def test_reservations_employee_user_get_nothing_from_StudentViewsOwnReservationList_view(groupEmployee):
    path = '/api/v1/reservation-student/'
    employee_test = mixer.blend(User)
    employee_test.groups.add(groupEmployee)
    employee_test.save()
    client = get_client(employee_test)
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'You do not have permission to perform this action.')


######################################################################################
######################## StudentAddReservationList ###################################
def test_reservations_anon_user_get_nothing_from_StudentAddReservationList_view():
    path = '/api/v1/reservation-student/add/'
    client = get_client()
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'credentials were not provided')


def test_reservations_student_user_get_nothing_from_StudentAddReservationList_view(student_house_reservation,groupStudent):
    path = '/api/v1/reservation-student/add/'
    student_test = mixer.blend(User)
    student_test.groups.add(groupStudent)
    student_test.save()
    client = get_client(student_test)
    response = client.post(path,
                           data={'neighborhood': '', 'room_type': '', 'student': student_house_reservation[0].user.pk, })
    assert response.status_code == HTTP_400_BAD_REQUEST

def test_reservations_student_user_can_not_create_wrong_reservation_from_StudentAddReservationList_view(student_house_reservation,groupStudent):
    path = '/api/v1/reservation-student/add/'
    student_test = mixer.blend(User)
    student_test.groups.add(groupStudent)
    student_test.save()
    client = get_client(student_test)
    response = client.post(path,
                           data={'neighborhood': '', 'room_type': 'SIN', 'student': student_house_reservation[0].user.pk, })
    assert response.status_code == HTTP_400_BAD_REQUEST
    response = client.post(path,
                           data={'neighborhood': 'PRV', 'room_type': 'SIN', 'student': student_house_reservation[0].user.pk, })
    assert response.status_code == HTTP_400_BAD_REQUEST
    response = client.post(path,
                           data={'neighborhood': 'PROVA', 'room_type': 'SIN', 'student': student_house_reservation[0].user.pk, })
    assert response.status_code == HTTP_400_BAD_REQUEST
    response = client.post(path,
                           data={'neighborhood': 'nrv', 'room_type': 'SIN', 'student': student_house_reservation[0].user.pk, })
    assert response.status_code == HTTP_400_BAD_REQUEST
    response = client.post(path,
                           data={'neighborhood': 'NRV', 'room_type': '', 'student': student_house_reservation[0].user.pk, })
    assert response.status_code == HTTP_400_BAD_REQUEST
    response = client.post(path,
                           data={'neighborhood': 'NRV', 'room_type': 'QWE', 'student': student_house_reservation[0].user.pk, })
    assert response.status_code == HTTP_400_BAD_REQUEST
    response = client.post(path,
                           data={'neighborhood': 'NRV', 'room_type': 'SINA', 'student': student_house_reservation[0].user.pk, })
    assert response.status_code == HTTP_400_BAD_REQUEST
    response = client.post(path,
                           data={'neighborhood': 'NRV', 'room_type': 'sin', 'student': student_house_reservation[0].user.pk, })
    assert response.status_code == HTTP_400_BAD_REQUEST

def test_reservations_employee_user_get_nothing_from_StudentAddReservationList_view(groupEmployee):
    path = '/api/v1/reservation-student/add/'
    employee_test = mixer.blend(User)
    employee_test.groups.add(groupEmployee)
    employee_test.save()
    client = get_client(employee_test)
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'You do not have permission to perform this action.')


######################################################################################
############################ StudentEditReservationList ##############################

def test_reservations_anon_user_get_nothing_from_StudentEditReservationList_view(student_house_reservation):
    path = '/api/v1/reservation-student/edit/' + str(student_house_reservation[0].pk) + '/'
    client = get_client()
    response = client.put(path,
                           data={'neighborhood': '', 'room_type': 'SIN', 'student': student_house_reservation[0].user.pk, })
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'credentials were not provided')


def test_reservations_student_user_get_nothing_from_StudentEditReservationList_view(student_house_reservation,groupStudent):
    path = '/api/v1/reservation-student/edit/' + str(student_house_reservation[0].pk) + '/'
    client = get_client(student_house_reservation[0].user)
    response = client.put(path,
                          data={'neighborhood': 'MTA', 'room_type': 'SIN',
                                'student': student_house_reservation[0].user.pk})
    assert response.status_code == HTTP_200_OK


def test_reservations_employee_user_get_nothing_from_StudentEditReservationList_view(student_house_reservation,groupEmployee):
    path = '/api/v1/reservation-student/edit/' + str(student_house_reservation[0].pk) + '/'
    employee = mixer.blend(User)
    employee.groups.add(groupEmployee)
    employee.save()
    client = get_client(employee)
    response = client.put(path,
                          data={'neighborhood': '', 'room_type': 'SIN',
                                'student': student_house_reservation[0].user.pk, })
    assert response.status_code == HTTP_403_FORBIDDEN

