from django.db.models import fields
from rest_framework.fields import ReadOnlyField
from rest_framework.relations import StringRelatedField
from timeline.models import UserTeam, UserProfile, TimeLineMessage
from rest_framework import serializers
from datetime import datetime
from django.utils.timesince import timesince


class TimeLineMessageSerializer(serializers.ModelSerializer):
    user_profile = serializers.StringRelatedField(read_only=True)
    since_publish = serializers.SerializerMethodField('get_since_publish')
    updated_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = TimeLineMessage
        # fields = '__all__'
        exclude = ['isDeleted', 'deleted_date']

    def get_since_publish(self, obj):
        return timesince(obj.created_date)


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    team = serializers.HyperlinkedRelatedField(
        view_name="team-detail", read_only=True)
    updated_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = UserProfile
        # fields = '__all__'
        exclude = ['isDeleted', 'deleted_date']


class UserTeamSerializer(serializers.ModelSerializer):
    team = serializers.StringRelatedField(many=True, read_only=True)
    updated_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = UserTeam
        # fields = '__all__'
        exclude = ['isDeleted', 'deleted_date']