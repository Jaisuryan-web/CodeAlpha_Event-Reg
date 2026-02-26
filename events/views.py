from rest_framework import generics
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Event, Registration
from .serializers import EventSerializer, RegistrationSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib import messages
from .forms import RegistrationForm

def home_view(request):
    return redirect('events')

def events_list(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'events/events_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    user_registered = False
    if request.user.is_authenticated:
        user_registered = Registration.objects.filter(user=request.user, event=event).exists()
    return render(request, 'events/event_detail.html', {
        'event': event,
        'user_registered': user_registered
    })

@login_required
def register_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    
    if Registration.objects.filter(user=request.user, event=event).exists():
        messages.warning(request, 'You are already registered for this event.')
        return redirect('event_detail', pk=pk)
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.user = request.user
            registration.event = event
            registration.save()
            messages.success(request, 'Successfully registered for the event!')
            return redirect('event_detail', pk=pk)
    else:
        form = RegistrationForm()
    
    return render(request, 'events/register_form.html', {
        'form': form,
        'event': event
    })

@login_required
def my_registrations(request):
    registrations = Registration.objects.filter(user=request.user).select_related('event')
    return render(request, 'events/my_registrations.html', {'registrations': registrations})

class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetailView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class RegisterEventView(generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]

class MyRegistrationsView(generics.ListAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Registration.objects.filter(user=self.request.user)
