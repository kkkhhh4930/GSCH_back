from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth import get_user_model

from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth import get_user_model

# 사용자 모델 가져오기
User = get_user_model()

# 사용자 시리얼라이저
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)  # 사용자의 username 필드만 포함

        # 필요한 경우 사용자의 다른 필드 추가 가능
        # fields = ('username', 'name', 'profile_img')


# 게시글 목록 조회 시리얼라이저
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content')


# 게시글 상세 조회 및 수정 시리얼라이저
class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # 읽기 전용 사용자 시리얼라이저
    class Meta:
        model = Article
        fields = 'all'
        read_only_fields = ('user',)
