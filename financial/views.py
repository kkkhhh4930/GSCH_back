import os
import requests
from .models import Deposit, DepositOption, Saving
from .serializers import DepositSerializer, DepositOptionSerializer
from .serializers import SavingSerializer, SavingOptionSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

API_KEY = 'u8Hi3CLUJFYx6KA3bbzHlUVqdQum5PdR'


def save_deposit_products(request):
    api_key = os.getenv('FINANCIAL_API_KEY')  # 환경 변수에서 API Key를 가져옴

    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    
    for li in response.get('result').get('baseList'):
        fin_prdt_cd = li.get('fin_prdt_cd')
        kor_co_nm = li.get('kor_co_nm')
        fin_prdt_nm = li.get('fin_prdt_nm')
        etc_note = li.get('etc_note')
        join_deny = li.get('join_deny')
        join_member = li.get('join_member')
        join_way = li.get('join_way')
        spcl_cnd = li.get('spcl_cnd')
    
            
        save_data = {
            'fin_prdt_cd' : fin_prdt_cd,
            'kor_co_nm' : kor_co_nm,
            'fin_prdt_nm' : fin_prdt_nm,
            'etc_note' : etc_note,
            'join_deny' : join_deny,
            'join_member' : join_member,
            'join_way' : join_way,
            'spcl_cnd' : spcl_cnd,
        }
        if Deposit.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
            continue  # 이미 존재하면 다음 데이터로 넘어감
            
        serializer = DepositSerializer(data = save_data)
        
        # 유효성 검증
        if serializer.is_valid(raise_exception=True):
            # 유효하다면 저장
            serializer.save()

    for option in response.get('result').get('optionList'):
        product = Deposit.objects.get(fin_prdt_cd=option.get('fin_prdt_cd'))
        option_save_data = {
        'fin_prdt_cd': option.get('fin_prdt_cd'),
        'intr_rate_type_nm': option.get('intr_rate_type_nm'),
        'intr_rate': option.get('intr_rate'),
        'intr_rate2': option.get('intr_rate2'),
        'save_trm': option.get('save_trm'),
        }

        optionserializer = DepositOptionSerializer(data=option_save_data)

        if optionserializer.is_valid(raise_exception=True):
            optionserializer.save(product=product)
                    
    # return JsonResponse(response)
    return JsonResponse({'message': 'Data saved successfully'})

@api_view(['GET']) # id 순
def deposit_list(request):
    deposits = Deposit.objects.all()
    serializer = DepositSerializer(deposits, many=True)
    return Response(serializer.data)