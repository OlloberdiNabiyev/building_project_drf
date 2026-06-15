from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register('buildings/',BuildingApiView)
router.register('companies/',CommentApiView)

urlpatterns = [
    path('buildings/<int:building_id>/comments/',CommentApiView.as_view({'get':'list','post': 'create'})),
    path('buildings/<int:building_id>/comments/<int:comment_id>/',CommentApiView.as_view({'get':'retrieve','partial_update':'patch','put':'update'})),
    path('',include(router.urls))
]