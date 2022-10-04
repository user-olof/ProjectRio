from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

member_list = views.MemberViewSet.as_view({
    'get': 'list'
})

member_detail = views.MemberViewSet.as_view({
    'get': 'retrieve'
})

# Create router and register our viewsets with it.
router = DefaultRouter()
router.register(r'members', views.MemberViewSet)
urlpatterns = router.urls
