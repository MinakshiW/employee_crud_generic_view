from django.urls import path
from .views import *

urlpatterns = [
    path('hv/', HomeView.as_view()),
    path('fv/', StudentCreateView.as_view()),
    path('sv/', StudentListView.as_view()),
    path('uv/<int:pk>/', StudentUpdateView.as_view()),
    path('dv/<int:pk>/', StudentDeleteView.as_view()),
]