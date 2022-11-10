
from . import views
from rest_framework.routers import DefaultRouter

events_and_classes_list = views.EventsAndClassesViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

events_and_classes_detail = views.EventsAndClassesViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

# Create router and register our viewset with it.
router = DefaultRouter()
router.register(r'events_and_classes', views.EventsAndClassesViewSet)
urlpatterns = router.urls

