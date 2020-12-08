import pytest
from django.core.exceptions import ValidationError
from mixer.backend.django import mixer


def test_allocations_wrong_neighborhood(db):
    allocation = mixer.blend('allocations.Allocation', neighborhood='BLA')
    with pytest.raises(ValidationError) as err:
        allocation.full_clean()


def test_allocation_correct_neighborhood_length(db):
    allocation = mixer.blend('allocations.Allocation')
    # print("LOCATION: " + allocation.neighborhood)
    assert allocation.neighborhood.__len__() == 3


# def test_allocation_correct_default_neighborhood(db):
#    allocation = mixer.blend('allocations.Allocation')
#    assert allocation.neighborhood == 'MTA'


def test_allocation_wrong_roomtype(db):
    allocation = mixer.blend('allocations.Allocation', room_type='MOU')
    with pytest.raises(ValidationError) as err:
        allocation.full_clean()


def test_allocation_correct_roomtype_length(db):
    allocation = mixer.blend('allocations.Allocation')
    assert allocation.room_type.__len__() == 3

# def test_allocation_correct_default_roomtype(db):
#    allocation = mixer.blend('allocations.Allocation')
#    assert allocation.room_type == 'SIN'
