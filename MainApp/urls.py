from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('add-client/', views.add_client, name='add-client'),
    path('edit-client-and-provider/<int:pk>/', views.edit_client_provider, name='edit_client_provider'),
    path('delete-client-and-provider/<int:pk>/', views.delete_client_provider, name='delete-client'),
    path('assigne-client-services/', views.assigne_services, name='assigne_services'),
]
