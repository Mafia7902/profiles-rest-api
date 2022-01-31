from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api.views import (
    HelloViewSet,
    UserProfileViewSet,
    HelloApiView,
    UserLoginApiView,
)

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, base_name='hello-viewset')
router.register('profile_viewset', UserProfileViewSet, base_name = 'UserProfileViewSet')


urlpatterns = [
    path('hello-view/', HelloApiView.as_view()),
    path('login/', UserLoginApiView.as_view()),
    path('', include(router.urls))
]

