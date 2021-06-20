from django.urls.conf import include, path
from rest_framework.routers import DefaultRouter
from timeline.api import views

router = DefaultRouter()
router.register(r'teams', views.TeamViewSet, basename="team",)
router.register(r'profiles', views.UserProfilesViewSet, basename="profile")
router.register(r'timeline', views.TimeLineViewSet, basename="timeline")

urlpatterns = [
    path('', include(router.urls))
]
