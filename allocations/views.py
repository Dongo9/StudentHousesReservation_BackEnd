# Create your views here.
from rest_framework import generics

from allocations.models import Allocation
from allocations.serializers import AllocationSerializer


class AllocationList(generics.ListCreateAPIView):
    # FINDALL
    queryset = Allocation.objects.all()
    serializer_class = AllocationSerializer


class AllocationDetail(generics.RetrieveUpdateDestroyAPIView):
    # ALLOWED OPERATIONS FOR A SINGLE ALLOCATION ONLY
    queryset = Allocation.objects.all()
    serializer_class = AllocationSerializer
