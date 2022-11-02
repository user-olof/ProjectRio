from rioacademy.apps.accounts import views
from rest_framework.routers import DefaultRouter

# account_detail = views.AccountViewSet.as_view({
#     'get': 'list',
#     'put': 'update',
# })

# Create router and register our viewsets with it
router = DefaultRouter()
router.register(r'accounts', views.AccountViewSet)
urlpatterns = router.urls