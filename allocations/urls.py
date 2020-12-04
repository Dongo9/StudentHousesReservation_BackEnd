from django.urls import path
from rest_framework.routers import SimpleRouter

from allocations.views import AllocationViewSet

# urlpatterns = [
#    path('<int:pk>/', AllocationDetail.as_view()),
#    path('', AllocationList.as_view()),
# ]

router = SimpleRouter()
router.register('', AllocationViewSet, basename='allocations')

urlpatterns = router.urls
