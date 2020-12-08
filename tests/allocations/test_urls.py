import json

import pytest
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

#PER L'HONEY POT NESSUNO HA MAI L'AUTORIZZAZIONE (TEST DICIAMO INUTILE)
def test_allocations_anon_user_get_nothing():
    path = reverse('allocations-list')
    client = get_client()
    response = client.get(path)
    print("PATH: " + path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'credentials were not provided')

#DA SISTEMARE
#DA PROVARE IN UNA PAGINA DOVE POSSIAMO ELENCARE TUTTI LE ALLOCATIONS (NELLA PAGINA ALLOCATIONS DA' 403 PERCHE' NESSUNO E' AUTORIZZATO)
def test_allocations_anon_user_get_nothing2(allocations):
    path = reverse('allocations-detail', kwargs={'pk': allocations[0].pk})
    client = get_client(allocations[0].student)
    response = client.get(path)
    assert response.status_code == HTTP_200_OK
    obj = parse(response)
    assert allocations[0].neighborhood.__len__() == 3

#DA COMPLETARE SECONDO I PERMESSI
def test_allocations_anon_user_get_nothing3():
    path = reverse('student-allocation-list')
    client = get_client()
    response = client.get(path)
    print("PATH: " + path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'credentials were not provided')
