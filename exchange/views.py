import requests
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import ExchangeRate
from .serializers import ExchangeRateSerializer
from rest_framework.response import Response

# Create your views here.
API_KEY = 'u8Hi3CLUJFYx6KA3bbzHlUVqdQum5PdR'  # 실제 API 키로 교체하세요
URL = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={API_KEY}&data=AP01'


    
@api_view(['GET'])
def exchange(request):
    # OpenAPI로부터 데이터 가져오기
    response = requests.get(URL).json()
    print(response)  # API 응답 출력

    # 이전 데이터 가져오기
    previous_data = ExchangeRate.objects.all()

    if response:  # API 응답이 있다면
        # 기존 데이터 삭제
        previous_data.delete()

        # 새로운 데이터 저장
        serializer = ExchangeRateSerializer(data=response, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    # 응답이 없거나 처리가 실패한 경우 기존 데이터를 반환
    serializer = ExchangeRateSerializer(previous_data, many=True)
    return Response(serializer.data)