from rest_framework import serializers
from .models import Profile,Project


class ProjectSerializer(serializers.ModelSerializer):





    class Meta:
        model = Project
        fields = ['name','description','design','usability','content','average','project_pic','link','profile_id']


class ProfileSerializer(serializers.ModelSerializer):
    projects = serializers.StringRelatedField(many=True,read_only=True)
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    profile_id = serializers.CharField(source='pk')

    class Meta:
        model = Profile
        fields = ['profile_id','user','profile_pic','bio','projects']

