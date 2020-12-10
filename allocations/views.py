# Create your views here.
from rest_framework import generics, viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from allocations.models import Allocation
from allocations.permissions import IsPermittedOnPostAndPermittedAuthor, IsTheCake, IsPermittedViewStudentsAllocations
from allocations.serializers import AllocationSerializer


class HoneyPotViewSet(viewsets.ModelViewSet):
    permission_classes = [IsTheCake, IsAuthenticated]
    serializer_class = AllocationSerializer

    def get_queryset(self):
        return None


# SAO: Student Administration Office
class SAOAllocationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsPermittedViewStudentsAllocations, IsAuthenticated]

    queryset = Allocation.objects.all()
    serializer_class = AllocationSerializer


class StudentAllocationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsPermittedOnPostAndPermittedAuthor]
    serializer_class = AllocationSerializer

    def get_queryset(self):
        return Allocation.objects.filter(student=self.request.user)
