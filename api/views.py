from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework.generics import get_object_or_404

class BuildingApiView(ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class CompanyApiView(ModelViewSet):
    queryset = ConstructionCompany.objects.all()
    serializer_class = CompanySerializer

class CommentApiView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        building_id = self.kwargs.get('building_id')
        return self.queryset.filter(building_id=building_id)

    def perform_create(self, serializer):
        building = get_object_or_404(Building,id=self.kwargs.get('building_id'))
        serializer.validated_data['user'] = self.request.user
        serializer.validated_data['building'] = building

        serializer.save()
        return serializer
