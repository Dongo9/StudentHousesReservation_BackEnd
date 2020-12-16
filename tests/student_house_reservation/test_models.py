import pytest
from django.core.exceptions import ValidationError
from mixer.backend.django import mixer

from student_house_reservation.models import Reservation


def test_allocations_wrong_neighborhood(db):
    allocation = mixer.blend('student_house_reservation.Reservation', neighborhood='BLA')
    with pytest.raises(ValidationError) as err:
        allocation.full_clean()


def test_allocation_wrong_roomtype(db):
    allocation = mixer.blend('student_house_reservation.Reservation', room_type='MOU')
    with pytest.raises(ValidationError) as err:
        allocation.full_clean()


def test_allocation_str(db):
    reservation = mixer.blend('student_house_reservation.Reservation')
    tostring = reservation.__str__()
    assert tostring == reservation.__str__()
