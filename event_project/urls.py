from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from events.views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('events.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='events/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='home', http_method_names=['get', 'post', 'options']), name='logout'),
]
