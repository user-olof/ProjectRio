from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

user_list = views.UserViewSet.as_view({
    'get': 'list'
})

user_detail = views.UserViewSet.as_view({'get': 'retrieve'})

# Create router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
urlpatterns = router.urls

# urlpatterns = [
#     path('users/', views.UserList.as_view(), name="user-list"),
#     path('users/<int:pk>/', views.UserDetail.as_view(), name="user-detail")
# ]