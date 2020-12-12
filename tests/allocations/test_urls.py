import json

import pytest
from django.contrib.auth.models import Group, Permission
from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_200_OK
from rest_framework.test import APIClient


@pytest.fixture()
def allocations(db):
    return [
        mixer.blend('allocations.Allocation'),
        mixer.blend('allocations.Allocation'),
        mixer.blend('allocations.Allocation'),
    ]


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


# PER L'HONEY POT NESSUNO HA MAI L'AUTORIZZAZIONE (TEST DICIAMO INUTILE)
def test_allocations_anon_user_get_nothing():
    path = reverse('allocations-list')
    client = get_client()
    response = client.get(path)
    print("PATH: " + path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'credentials were not provided')


# PER SAO-ALLOCATIONS
def test_SAO_allocations_anon_user_get_nothing():
    path = reverse('SAO-allocations-list')
    client = get_client()
    response = client.get(path)
    print("PATH: " + path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'credentials were not provided')


# PER ALLOCATIONS STUDENTE
def test_student_allocations_anon_user_get_nothing():
    path = reverse('student-allocation-perm-list')
    client = get_client()
    response = client.get(path)
    print("PATH: " + path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'credentials were not provided')


def test_allocations_student_gets_his_allocation_details(allocations):
    path = reverse('student-allocation-perm-detail', kwargs={'pk': allocations[0].pk})
    group = Group(name='Students')
    group.save()
    perm = Permission.objects.get(name='Can view allocation')
    group.permissions.add(perm)
    prova = allocations[0].student
    prova.groups.add(group)
    prova.save()
    client = get_client(prova)
    response = client.get(path)
    assert response.status_code == HTTP_200_OK
    obj = parse(response)
    assert allocations[0].neighborhood.__len__() == 3


