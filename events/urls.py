from django.urls import path
from .views import (
    EventListView, EventDetailView, RegisterEventView, MyRegistrationsView, 
    home_view, events_list, event_detail, register_event, my_registrations
)

urlpatterns = [
    path('events/', events_list, name='events'),
    path('events/<int:pk>/', event_detail, name='event_detail'),
    path('events/<int:pk>/register/', register_event, name='register_event'),
    path('my-registrations/', my_registrations, name='my_registrations'),
]
