from django.urls import path
from . import views

urlpatterns = [
    path('deposit_list/', views.deposit_list),
    path('deposit_list/<str:deposit_code>/', views.deposit_detail),
    path('deposit_list/<str:deposit_code>/option_list/', views.deposit_option_list),
    path('deposit_list/<str:deposit_code>/option_list/<int:deposit_option_pk>/', views.deposit_option_detail),
    path('saving_list/', views.saving_list),
    path('saving_list/<str:saving_code>/', views.saving_detail),
    path('saving_list/<str:saving_code>/option_list/', views.saving_option_list),
    path('saving_list/<str:saving_code>/option_list/<int:saving_option_pk>/', views.saving_option_detail),
    path('save_deposit_products/', views.save_deposit_products, name='save_deposit_products'),
    path('save_saving_products/', views.save_saving_products, name='save_saving_products'),
]
