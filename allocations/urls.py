from django.urls import path
from rest_framework.routers import SimpleRouter

from allocations.views import AllocationViewSet, PreferencesByStudentViewSet, PreferencesStudent

# urlpatterns = [
#    path('<int:pk>/', AllocationDetail.as_view()),
#    path('', AllocationList.as_view()),
# ]

router = SimpleRouter()
router.register('by-student', PreferencesByStudentViewSet, basename='allocations-by-student')
router.register('', AllocationViewSet, basename='allocations')
router.register('editor', PreferencesStudent, basename='allocation-by-groups')


urlpatterns = router.urls
