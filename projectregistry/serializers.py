from rest_framework import serializers
from .models import Project

# Create your serializers here
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'language', 'created_at', 'MedalType', 'medal')
        read_only_fields = ('created_at', )
