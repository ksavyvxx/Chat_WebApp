from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('chat/', views.home, name='chat'),
    path('message/<int:pk>/edit/', views.edit_message, name='edit_message'),
    path('message/<int:pk>/delete/', views.delete_message, name='delete_message'),
    path('message/<int:pk>/restore/', views.restore_message, name='restore_message'),
]