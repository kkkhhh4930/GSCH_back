from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('<str:username>/profile/', views.user_info_profile),
    path('change-password/', views.change_password, name='change_password'),
]
