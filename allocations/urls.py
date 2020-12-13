# from django.urls import path
from rest_framework.routers import SimpleRouter


# MIND THE URLS ORDER! (empty url '' at the end)
from allocations.views import StudentAllocationViewSet, SAOAllocationViewSet, \
    HoneyPotViewSet

# URLS HAVE TO BE CONSIDERED AFTER http://127.0.0.1:8000/api/v1/allocations/
router = SimpleRouter()
# TODO students can only modify our one and only allocation
router.register('student-allocation', StudentAllocationViewSet, basename='student-allocation-perm')
# Student Administration Office page that can only view all student's allocations
router.register('SAO-allocations', SAOAllocationViewSet, basename='SAO-allocations')
# HoneyPot url
router.register('', HoneyPotViewSet, basename='allocations')

urlpatterns = router.urls
