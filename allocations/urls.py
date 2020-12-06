# from django.urls import path
from rest_framework.routers import SimpleRouter

from allocations.views import AllocationViewSet, PreferencesByStudentViewSet, PreferencesEditorViewSet, \
    PostAllocationPermissionViewSet, StudentAllocationViewSet

# urlpatterns = [
#    path('<int:pk>/', AllocationDetail.as_view()),
#    path('', AllocationList.as_view()),
# ]

# MIND THE URLS ORDER! (empty url '' at the end)
router = SimpleRouter()
router.register('by-student', PreferencesByStudentViewSet, basename='allocations-by-student')
router.register('editor', PreferencesEditorViewSet, basename='editor-allocationOnRole-students')
router.register('allocation-perm', PostAllocationPermissionViewSet, basename='allocation-perm')
router.register('student-allocation', StudentAllocationViewSet, basename='student-allocation-perm') # URL DEFINITIVO PER STUDENTE CHE VEDE SUA PREFERENZA
router.register('', AllocationViewSet, basename='allocations')


urlpatterns = router.urls
