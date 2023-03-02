from apps.accounts import views
from rest_framework.routers import DefaultRouter

account_detail = views.AccountViewSet.as_view({
    'get' : 'retrieve',
    'post': 'create'

})

account_list = views.AccountViewSet.as_view({
    'get' : 'list' 
})

    
# Create router and register our viewsets with it
router = DefaultRouter()
router.register(r'accounts', views.AccountViewSet, basename='account')
urlpatterns = router.urls