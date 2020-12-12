from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Allocation(models.Model):
    # ENUMS DEFINITION
    class Neighborhood(models.TextChoices):
        NERVOSO = 'NRV', _('Nervoso')
        MARTENSSON_A = 'MTA', _('MartenssonA')
        MARTENSSON_B = 'MTB', _('MartenssonB')
        MOLICELLE_A = 'MLA', _('MolicelleA')
        MOLICELLE_B = 'MLB', _('MolicelleB')
        MAISONETTES = 'MSN', _('Maisonettes')
        CHIODO_1 = 'CH1', _('Chiodo1')
        CHIODO_2 = 'CH2', _('Chiodo2')
        MONACI = 'MON', _('Monaci')
        SAN_GENNARO = 'SNG', _('SanGennaro')

    class RoomType(models.TextChoices):
        SINGLE = 'SIN', _('Single')
        DOUBLE = 'DBL', _('Double')

    # FIELDS DEFINITION BASED ON PREVIOUS ENUMS
    neighborhood = models.CharField(
        max_length=3,
        choices=Neighborhood.choices,
        #default=Neighborhood.MARTENSSON_A,
    )

    room_type = models.CharField(
        max_length=3,
        choices=RoomType.choices,
        #default=RoomType.SINGLE,
    )

    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    # AS JAVA TOSTRING
    def __str__(self):
        return self.neighborhood + " " + self.room_type + " " + self.student.__str__()
