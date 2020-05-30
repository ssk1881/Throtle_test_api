from rest_framework import serializers

from .models import ActivityPeriod, User


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    activity_periods = ActivitySerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ('id', 'real_name', 'tz', 'activity_periods')
        read_only_fields = ('id', 'real_name', 'tz', 'activity_periods')



