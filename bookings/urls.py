from pathlib import Path
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # ex: /bookings/
    path("",views.MemberList.as_view(), name="member_list"),
    # ex: /bookings/1/
    #path("<int:member_id>/",views.detail, name='detail'),
    # ex: /bookings/1/
    path("<int:pk>/", views.MemberDetail.as_view(), name='member_detail'),
    path('', views.UserList.as_view(), name="user_list"),
    path('<int:pk>/', views.UserDetail.as_view(), name="user_detail")
]

urlpatterns = format_suffix_patterns(urlpatterns)