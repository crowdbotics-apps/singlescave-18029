from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    SettingViewSet,
    ProfileViewSet,
    InboxViewSet,
    DislikeViewSet,
    MatchViewSet,
    UserPhotoViewSet,
    LikeViewSet,
)

router = DefaultRouter()
router.register("dislike", DislikeViewSet)
router.register("profile", ProfileViewSet)
router.register("setting", SettingViewSet)
router.register("userphoto", UserPhotoViewSet)
router.register("like", LikeViewSet)
router.register("match", MatchViewSet)
router.register("inbox", InboxViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
