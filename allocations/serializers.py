from rest_framework import serializers

from allocations.models import Allocation


class AllocationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'neighborhood', 'room_type', 'student')
        model = Allocation
