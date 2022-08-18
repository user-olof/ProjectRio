from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # ex: /bookings/
    path("",views.bookings_list, name="bookings"),
    # ex: /bookings/1/
    #path("<int:member_id>/",views.detail, name='detail'),
    # ex: /bookings/1/
    path("<int:pk>/", views.bookings_detail, name='bookings_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)