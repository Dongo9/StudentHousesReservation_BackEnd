from django.urls import path

from allocations.views import AllocationDetail, AllocationList

urlpatterns = [
    path('<int:pk>/', AllocationDetail.as_view()),
    path('', AllocationList.as_view()),
]
