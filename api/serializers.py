from rest_framework import serializers

from .models import *

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '_all_'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstructionCompany
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

