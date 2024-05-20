from django.urls import path
from . import views


urlpatterns = [
    path('save_deposit_products', views.save_deposit_products),
    path('deposit_list/', views.deposit_list),
]