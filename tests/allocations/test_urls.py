import json

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission, User
from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework.status import *
from rest_framework.test import APIClient


@pytest.fixture()
def allocations(db):
    return [
        mixer.blend('allocations.Allocation') for _ in range(3)
    ]


@pytest.fixture()
def groupStudent(db):
    group = Group(name='Students')
    group.save()
    perm = Permission.objects.get(name='Can view allocation')
    group.permissions.add(perm)
    return group


@pytest.fixture()
def groupAdministrator(db):
    group = Group(name='Administration')
    group.save()
    perm = Permission.objects.get(name='Can view allocation')
    group.permissions.add(perm)
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


###USER NOT AUTHENTICATED### => OK

##TO LISTS##

# TO HONEY POT => OK
def test_allocations_anon_user_get_nothing_from_honeypot_list():
    path = reverse('allocations-list')
    client = get_client()
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'credentials were not provided')


# TO STAFF VIEW=> OK
def test_SAO_allocations_anon_user_get_nothing_from_staff_view_list():
    path = reverse('SAO-allocations-list')
    client = get_client()
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'credentials were not provided')


# TO STUDENT_VIEW => OK
def test_student_allocations_anon_user_get_nothing_from_student_view_list():
    path = reverse('student-allocation-perm-list')
    client = get_client()
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'credentials were not provided')


##TO DETAIL## => OK

# TO HONEY POT => OK
def test_allocations_anon_user_get_nothing_from_honeypot_detail(allocations):
    path = reverse('allocations-detail', kwargs={'pk': allocations[0].pk})
    client = get_client()
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'credentials were not provided')


# TO STAFF VIEW=> OK
def test_SAO_allocations_anon_user_get_nothing_from_staff_view_detail(allocations):
    path = reverse('SAO-allocations-detail', kwargs={'pk': allocations[0].pk})
    client = get_client()
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'credentials were not provided')


# TO STUDENT_VIEW=> OK
def test_student_allocations_anon_user_get_nothing_from_student_view_detail(allocations):
    path = reverse('student-allocation-perm-detail', kwargs={'pk': allocations[0].pk})
    client = get_client()
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'credentials were not provided')


###AUTHENTICATED STUDENT###

##TO LISTS## => OK

# TO HONEY POT => OK
def test_allocations_student_get_nothing_from_honeypot_list(groupStudent):
    path = reverse('allocations-list')
    allocation_test = mixer.blend('allocations.Allocation')
    student_test = allocation_test.student
    student_test.groups.add(groupStudent)
    student_test.save()
    client = get_client(student_test)
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'You do not have permission to perform this action.')


# TO STAFF VIEW => 0K
def test_SAO_allocations_student_get_nothing_from_staff_view_list(groupStudent):
    path = reverse('SAO-allocations-list')
    allocation_test = mixer.blend('allocations.Allocation')
    student_test = allocation_test.student
    student_test.groups.add(groupStudent)
    student_test.save()
    client = get_client(student_test)
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'You do not have permission to perform this action.')


# TO STUDENT VIEW: HIS OWN ALLOCATIONS LIST=> OK
def test_student_allocations_student_gets_his_allocation_list(allocations, groupStudent):
    path = reverse('student-allocation-perm-list')
    student_test = allocations[0].student
    student_test.groups.add(groupStudent)
    student_test.save()
    client = get_client(student_test)
    response = client.get(path)
    assert response.status_code == HTTP_200_OK


##TO DETAIL## => OK

# TO HONEY POT => OK
def test_allocations_student_get_nothing_from_honeypot_detail(allocations, groupStudent):
    path = reverse('allocations-detail', kwargs={'pk': allocations[0].pk})
    student_test = allocations[0].student
    student_test.groups.add(groupStudent)
    student_test.save()
    client = get_client(student_test)
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'You do not have permission to perform this action.')


# TO STAFF VIEW => 0K
def test_SAO_allocations_student_get_nothing_from_staff_view_detail(allocations, groupStudent):
    path = reverse('SAO-allocations-detail', kwargs={'pk': allocations[0].pk})
    student_test = allocations[0].student
    student_test.groups.add(groupStudent)
    student_test.save()
    client = get_client(student_test)
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'You do not have permission to perform this action.')


# TO STUDENT VIEW: HIS OWN ALLOCATIONS => OK
def test_student_allocations_student_gets_his_allocation_detail(allocations, groupStudent):
    path = reverse('student-allocation-perm-detail', kwargs={'pk': allocations[0].pk})
    student_test = allocations[0].student
    student_test.groups.add(groupStudent)
    student_test.save()
    client = get_client(student_test)
    response = client.get(path)
    assert response.status_code == HTTP_200_OK


###AUTHENTICATED STAFF MEMBER###

##TO LISTS##

# TO HONEY POT => OK
def test_allocations_administrator_get_nothing_from_honeypot_list(groupAdministrator):
    path = reverse('allocations-list')
    administrator_test = mixer.blend(User)
    administrator_test.groups.add(groupAdministrator)
    administrator_test.save()
    client = get_client(administrator_test)
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'You do not have permission to perform this action.')


# TO STAFF VIEW => OK
def test_SAO_allocations_administrator_get_the_allocations_from_staff_view_list(groupAdministrator):
    path = reverse('SAO-allocations-list')
    administrator_test = mixer.blend(User)
    administrator_test.groups.add(groupAdministrator)
    administrator_test.save()
    client = get_client(administrator_test)
    response = client.get(path)
    assert response.status_code == HTTP_200_OK


# TO STUDENT VIEW => OK
def test_student_allocations_administrator_gets_nothing_from_student_view_list(groupAdministrator):
    path = reverse('student-allocation-perm-list')
    administrator_test = mixer.blend(User)
    administrator_test.groups.add(groupAdministrator)
    administrator_test.save()
    client = get_client(administrator_test)
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'You do not have permission to perform this action.')


##TO DETAIL##

# TO HONEY POT => OK
def test_allocations_administrator_get_nothing_from_honeypot_detail(allocations, groupAdministrator):
    path = reverse('allocations-detail', kwargs={'pk': allocations[0].pk})
    administrator_test = mixer.blend(User)
    administrator_test.groups.add(groupAdministrator)
    administrator_test.save()
    client = get_client(administrator_test)
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'You do not have permission to perform this action.')


# TO STAFF VIEW
def test_SAO_allocations_administrator_get_nothing_from_staff_view_detail(allocations, groupAdministrator):
    path = reverse('SAO-allocations-detail', kwargs={'pk': allocations[0].pk})
    administrator_test = mixer.blend(User)
    administrator_test.groups.add(groupAdministrator)
    administrator_test.save()
    client = get_client(administrator_test)
    response = client.get(path)
    assert response.status_code == HTTP_200_OK


# TO STUDENT VIEW => 0K
def test_student_allocations_administrator_nothing_from_student_view_detail(allocations, groupAdministrator):
    path = reverse('student-allocation-perm-detail', kwargs={'pk': allocations[0].pk})
    administrator_test = mixer.blend(User)
    administrator_test.groups.add(groupAdministrator)
    administrator_test.save()
    client = get_client(administrator_test)
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'You do not have permission to perform this action.')


def test_allocation_student_can_create_correct_allocation(allocations, groupStudent):
    path = reverse('student-allocation-perm-list')
    student_test = allocations[0].student
    student_test.groups.add(groupStudent)
    student_test.save()
    client = get_client(student_test)
    response = client.post(path,
                           data={'neighborhood': 'NRV', 'room_type': 'SIN', 'student': allocations[0].student.pk, })
    assert response.status_code == HTTP_201_CREATED


def test_allocation_student_can_create_correct_allocation2(allocations, groupAdministrator):
    path = reverse('SAO-allocations-list')
    administrator_test = mixer.blend(User)
    administrator_test.groups.add( )
    administrator_test.save()
    client = get_client(administrator_test)
    response = client.post(path,
                           data={'neighborhood': 'NRV', 'room_type': 'SIN', 'student': allocations[0].student.pk, })
    assert response.status_code == HTTP_201_CREATED


def test_allocation_student_can_not_create_wrong_by_neighborhood_allocation(allocations, groupStudent):
    path = reverse('student-allocation-perm-list')
    student_test = allocations[0].student
    student_test.groups.add(groupStudent)
    student_test.save()
    client = get_client(student_test)
    response = client.post(path,
                           data={'neighborhood': '', 'room_type': 'SIN', 'student': allocations[0].student.pk, })
    assert response.status_code == HTTP_400_BAD_REQUEST
    response = client.post(path,
                           data={'neighborhood': 'PRV', 'room_type': 'SIN', 'student': allocations[0].student.pk, })
    assert response.status_code == HTTP_400_BAD_REQUEST
    response = client.post(path,
                           data={'neighborhood': 'PROVA', 'room_type': 'SIN', 'student': allocations[0].student.pk, })
    assert response.status_code == HTTP_400_BAD_REQUEST
    response = client.post(path,
                           data={'neighborhood': 'nrv', 'room_type': 'SIN', 'student': allocations[0].student.pk, })
    assert response.status_code == HTTP_400_BAD_REQUEST


def test_allocation_student_can_not_create_wrong_by_roomtype_allocation(allocations, groupStudent):
    path = reverse('student-allocation-perm-list')
    student_test = allocations[0].student
    student_test.groups.add(groupStudent)
    student_test.save()
    client = get_client(student_test)
    response = client.post(path,
                           data={'neighborhood': 'NRV', 'room_type': '', 'student': allocations[0].student.pk, })
    assert response.status_code == HTTP_400_BAD_REQUEST
    response = client.post(path,
                           data={'neighborhood': 'NRV', 'room_type': 'QWE', 'student': allocations[0].student.pk, })
    assert response.status_code == HTTP_400_BAD_REQUEST
    response = client.post(path,
                           data={'neighborhood': 'NRV', 'room_type': 'SINA', 'student': allocations[0].student.pk, })
    assert response.status_code == HTTP_400_BAD_REQUEST
    response = client.post(path,
                           data={'neighborhood': 'NRV', 'room_type': 'sin', 'student': allocations[0].student.pk, })
    assert response.status_code == HTTP_400_BAD_REQUEST
