from django.urls import path
from . import views


urlpatterns = [
    path('deposit_list/', views.save_deposit_products),
    # path('deposit_list/<str:deposit_code>/', views.deposit_detail),
]