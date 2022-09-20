from django.urls import path
from . import views

urlpatterns = [
    # path('', views.api_root),
    path('events_and_classes/', views.EventsAndClassesList.as_view(), name="events_and_classes-list"),
    path('events_and_classes/<int:pk>/', views.EventsAndClassesDetail.as_view()),
    path('events_and_classes/<int:pk>/name/', views.EventsAndClassesName.as_view())
    # ex: /bookings/
    # path("",views.MemberList.as_view(), name="member_list"),
    # ex: /bookings/1/
    #path("<int:member_id>/",views.detail, name='detail'),
    # ex: /bookings/1/
    # path("<int:pk>/", views.MemberDetail.as_view(), name='member_detail'),

    
]


# urlpatterns = format_suffix_patterns(urlpatterns)