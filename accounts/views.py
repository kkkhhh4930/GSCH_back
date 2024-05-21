from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .serializers import UserProfileSerializer, UserInfoSerializer

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def user_info_profile(request, username):
    print("user_info_profile called with username:", username)
    user = get_object_or_404(get_user_model(), username=username)
    
    if request.user.username == username:
        if request.method == 'GET':
            serializer = UserProfileSerializer(user)
            print("Serialized user data:", serializer.data)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            data = {
                'profile_img': request.data.get('profile_img'),
                'email': request.data.get('email'),
                'age': request.data.get('age'),
                'money': request.data.get('money'),
                'salary': request.data.get('salary')
            }
            serializer = UserInfoSerializer(instance=user, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    user = request.user
    old_password = request.data.get('old_password')
    new_password = request.data.get('new_password')
    if not user.check_password(old_password):
        return Response({'detail': '기존 비밀번호가 올바르지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    user.password = make_password(new_password)
    user.save()
    return Response({'detail': '비밀번호가 성공적으로 변경되었습니다.'}, status=status.HTTP_200_OK)