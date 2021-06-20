from django.utils import tree
from rest_framework.settings import perform_import
from timeline.api.pagination import SmallPagination
from rest_framework import generics, request
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework import mixins
from timeline.models import UserProfile, UserTeam, TimeLineMessage
from timeline.api.serializers import UserTeamSerializer, UserProfileSerializer, TimeLineMessageSerializer
from timeline.api.permissions import isAdminOrReadOnly, isProfileOwnerOrReadonly, isTimeLineMessageOwnerOrReadonly
from datetime import datetime


class TeamViewSet(ModelViewSet):
    queryset = UserTeam.objects.all()
    serializer_class = UserTeamSerializer
    permission_classes = [isAdminOrReadOnly]
    pagination_class = SmallPagination

    def perform_update(self, serializer):
        now = datetime.now()
        serializer.save(updated_date=now)


class UserProfilesViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [isProfileOwnerOrReadonly]
    pagination_class = SmallPagination

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(User=user)

    def perform_update(self, serializer):
        now = datetime.now()
        serializer.save(updated_date=now)


class TimeLineViewSet(ModelViewSet):
    queryset = TimeLineMessage.objects.all().order_by("-created_date")
    serializer_class = TimeLineMessageSerializer
    permission_classes = [isTimeLineMessageOwnerOrReadonly]
    pagination_class = SmallPagination

    def perform_create(self, serializer):
        user_profile = self.request.user.userprofile
        serializer.save(user_profile=user_profile)

    def perform_update(self, serializer):
        now = datetime.now()
        serializer.save(updated_date=now)
