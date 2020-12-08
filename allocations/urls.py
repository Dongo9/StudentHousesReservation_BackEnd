# from django.urls import path
from rest_framework.routers import SimpleRouter

from allocations.views import SAOAllocationViewSet, StudentAllocationViewSet, HoneyPotViewSet

# MIND THE URLS ORDER! (empty url '' at the end)
router = SimpleRouter()
router.register('student-allocation', StudentAllocationViewSet,
                basename='student-allocation-perm')  # TODO students can only modify our one and only allocation
router.register('SAO-allocations-list', SAOAllocationViewSet,
                basename='allocations')  # Student Administration Office page that can only view all student's allocations
router.register('', HoneyPotViewSet, basename='allocations')  # HoneyPot url

urlpatterns = router.urls
