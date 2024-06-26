from django.urls import path
from . import views


urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('articles/<int:article_pk>/comments/', views.comment_list),
    path('articles/<int:article_pk>/comments/<int:comment_pk>/', views.comment_detail),  # 수정된 URL 패턴
]