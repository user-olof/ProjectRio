
from . import views
from rest_framework.routers import DefaultRouter


booking_list = views.BookingViewSet.as_view({
    'post': 'create', 
    'get': 'list'
})

booking_detail = views.BookingViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'

})

booking_book = views.BookingViewSet.as_view({
    'get': 'book'
})

# Create router and register our viewsets with it.
router = DefaultRouter()
router.register(r'bookings', views.BookingViewSet, basename='booking')
urlpatterns = router.urls
