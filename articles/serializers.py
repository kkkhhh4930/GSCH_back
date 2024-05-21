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
    user = UserSerializer(read_only=True)  # 읽기 전용 사용자 시리얼라이저
    class Meta:
        model = Article
        fields = ('id', 'title', 'user',)  # 게시글의 id, 제목 및 작성자(사용자) 포함


# 게시글 상세 조회 및 수정 시리얼라이저
class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # 읽기 전용 사용자 시리얼라이저
    class Meta:
        model = Article
        fields = '__all__'  # 모든 게시글 필드를 포함


# 댓글 시리얼라이저
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # 읽기 전용 사용자 시리얼라이저
    class Meta:
        model = Comment
        fields = '__all__'  # 모든 댓글 필드를 포함
        read_only_fields = ('article',)  # article 필드는 읽기 전용으로 설정