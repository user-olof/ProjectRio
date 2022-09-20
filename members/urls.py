from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.MemberList.as_view(), name="member-list"),
    path('members/<int:pk>/', views.MemberDetail.as_view(), name="member-details")
]