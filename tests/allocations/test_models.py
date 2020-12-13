import pytest
from django.core.exceptions import ValidationError
from mixer.backend.django import mixer


def test_allocations_wrong_neighborhood(db):
    allocation = mixer.blend('allocations.Allocation', neighborhood='BLA')
    with pytest.raises(ValidationError) as err:
        allocation.full_clean()


def test_allocation_wrong_roomtype(db):
    allocation = mixer.blend('allocations.Allocation', room_type='MOU')
    with pytest.raises(ValidationError) as err:
        allocation.full_clean()
