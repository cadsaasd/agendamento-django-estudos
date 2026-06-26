"""
URL configuration for login app.
"""
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.login_view)
]
