from django.urls import path
from . import views


urlpatterns = [
    path('deposit_list/', views.deposit_list),
    # path('deposit_list/<str:deposit_code>/', views.deposit_detail),
]