from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment


# Article 목록 조회 및 생성
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
        # 모든 Article을 조회
        articles = get_list_or_404(Article)
        # 조회된 Article을 시리얼라이즈
        serializer = ArticleListSerializer(articles, many=True)
        # 시리얼라이즈된 데이터를 JSON 형태로 반환
        return Response(serializer.data)

    elif request.method == 'POST':
        # 클라이언트로부터 전달된 데이터를 시리얼라이즈
        serializer = ArticleSerializer(data=request.data)
        print(request.data )
        print(request.user )
        # 데이터가 유효한 경우 저장
        if serializer.is_valid(raise_exception=True):
            # 로그인한 사용자를 Article의 작성자로 지정하여 저장
            print('Pass')
            serializer.save(user=request.user)
            # 저장된 데이터를 JSON 형태로 반환
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 특정 Article 조회, 수정 및 삭제
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, article_pk):
    # 특정 pk를 가진 Article을 조회
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        # 조회된 Article을 시리얼라이즈
        serializer = ArticleSerializer(article)
        # 시리얼라이즈된 데이터를 JSON 형태로 반환
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        if request.user.is_authenticated:
            # 로그인한 사용자가 Article 작성자인 경우 삭제
            if request.user == article.user:
                article.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "인증 자격 증명이 제공되지 않았습니다."}, status=status.HTTP_401_UNAUTHORIZED)
    
    elif request.method == 'PUT':
        if request.user.is_authenticated:
            # 클라이언트로부터 전달된 데이터로 Article을 부분적으로 업데이트
            serializer = ArticleSerializer(instance=article, data=request.data, partial=True)
            # 데이터가 유효한 경우 저장
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                # 저장된 데이터를 JSON 형태로 반환
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "인증 자격 증명이 제공되지 않았습니다."}, status=status.HTTP_401_UNAUTHORIZED)


# 특정 Article에 대한 Comment 목록 조회
@api_view(['GET'])
def comment_list(request, article_pk):
    # 특정 pk를 가진 Article을 조회
    article = get_object_or_404(Article, pk=article_pk)
    
    if request.method == 'GET':
        # 해당 Article에 대한 모든 Comment를 조회
        comments = article.comment_set.all()
        # 조회된 Comment를 시리얼라이즈
        serializer = CommentSerializer(comments, many=True)
        # 시리얼라이즈된 데이터를 JSON 형태로 반환
        return Response(serializer.data)


# 특정 Comment 조회, 수정 및 삭제
@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def comment_detail(request, article_pk, comment_pk):
    # 특정 pk를 가진 Comment를 조회
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.method == 'GET':
        # 조회된 Comment를 시리얼라이즈
        serializer = CommentSerializer(comment)
        # 시리얼라이즈된 데이터를 JSON 형태로 반환
        return Response(serializer.data)

    elif request.method == 'DELETE':
        # 로그인한 사용자가 Comment 작성자인 경우 삭제
        if request.user == comment.user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "댓글 작성자가 아닙니다."}, status=status.HTTP_401_UNAUTHORIZED)
    
    elif request.method == 'PUT':
        # 로그인한 사용자가 Comment 작성자인 경우 업데이트
        if request.user == comment.user:
            # 클라이언트로부터 전달된 데이터로 Comment를 부분적으로 업데이트
            serializer = CommentSerializer(instance=comment, data=request.data, partial=True)
            # 데이터가 유효한 경우 저장
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                # 저장된 데이터를 JSON 형태로 반환
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "댓글 작성자가 아닙니다."}, status=status.HTTP_401_UNAUTHORIZED)


# 새로운 Comment 생성
@api_view(['POST'])
def comment_create(request, article_pk):
    # 특정 pk를 가진 Article을 조회
    article = get_object_or_404(Article, pk=article_pk)
    
    if request.user.is_authenticated:
        # 클라이언트로부터 전달된 데이터를 시리얼라이즈
        serializer = CommentSerializer(data=request.data)
        # 데이터가 유효한 경우 저장
        if serializer.is_valid(raise_exception=True):
            # 로그인한 사용자를 Comment의 작성자로 지정하여 저장
            serializer.save(article=article, user=request.user)
            # 저장된 데이터를 JSON 형태로 반환
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response({"detail": "인증 자격 증명이 제공되지 않았습니다."}, status=status.HTTP_401_UNAUTHORIZED)