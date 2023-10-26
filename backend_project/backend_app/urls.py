from django.urls import include, path
from . import views

urlpatterns = [
    path('userURLs/', views.UserURLView.as_view(), name="userURL")
]