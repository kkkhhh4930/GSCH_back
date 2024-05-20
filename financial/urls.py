from django.urls import path
from . import views

app_name = 'finlife'

urlpatterns = [
    path('save_deposit_products/', views.save_deposit_products),
    path('save_saving_products/', views.save_saving_products),
    
    path('deposit_list/', views.deposit_list),
    path('saving_list/', views.saving_list),
    
    path('deposit_list/<str:fin_prdt_cd>/', views.deposit_detail, name='deposit_detail'),
    path('deposit_list/<str:fin_prdt_cd>/option_list/', views.depositOption_list),


]