# Create your views here.
from rest_framework import generics, viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from allocations.models import Allocation
from allocations.permissions import IsPreferenceAuthorOrReadOnly, IsPreferenceAuthor
from allocations.serializers import AllocationSerializer


# class AllocationList(generics.ListCreateAPIView):
#    # FINDALL
#    queryset = Allocation.objects.all()
#    serializer_class = AllocationSerializer


# class AllocationDetail(generics.RetrieveUpdateDestroyAPIView):
# ALLOWED OPERATIONS FOR A SINGLE ALLOCATION ONLY
#    queryset = Allocation.objects.all()
#    serializer_class = AllocationSerializer

class AllocationViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [IsPreferenceAuthorOrReadOnly, IsAuthenticated]

    queryset = Allocation.objects.all()
    serializer_class = AllocationSerializer


class PreferencesByStudentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = AllocationSerializer

    def get_queryset(self):
        return Allocation.objects.filter(student=self.request.user)


class PreferencesStudent(viewsets.ModelViewSet):
    permission_classes = [IsPreferenceAuthor]
    queryset = Allocation.objects.all()
    serializer_class = AllocationSerializer
