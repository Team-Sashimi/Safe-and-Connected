from rest_framework import serializers
from .models import Event, EventRoster, Lang, ClientProfile, OrganizationProfile
from .models import OrganizationMembership, ClientLanguageMembership, ManagerOrgMembership
from .models import OrgLanguageMembership, EventType, FileUpload, User
from djoser.serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('email', 'username', 'role', 'password', 'id')


class UserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = ('email', 'username', 'role', 'id')


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'


class EventRosterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['event_attendees']


class EventRosterSignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventRoster
        fields = ['event_id']


class LangSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lang
        fields = '__all__'


class ClientProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientProfile
        fields = '__all__'


class OrganizationProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizationProfile
        fields = '__all__'


class OrganizationMembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizationMembership
        fields = '__all__'

# class ManagerMembershipSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = ManagerOrgMembership
#         fields = '__all__'


class ClientLanguageMembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientLanguageMembership
        fields = '__all__'


class OrgLanguageMembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrgLanguageMembership
        fields = '__all__'


class EventTypeSerializers(serializers.ModelSerializer):

    class Meta:
        model = EventType
        fields = '__all__'


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = [
            "id",
            "client_profile",
            "organization_profile",
            "event",
            "file",
        ]


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationMembership
        fields = '__all__'
