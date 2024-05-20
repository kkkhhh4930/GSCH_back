import requests
from .models import Deposit, DepositOption, Saving, SavingOption
from django.shortcuts import get_object_or_404
from .serializers import DepositSerializer, DepositOptionSerializer
from .serializers import SavingSerializer, SavingOptionSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from pprint import pprint

# 금융감독원 API
API_KEY = '05123616ac0af1b386553f893c720f21'
URL= f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'

@api_view(['GET'])
def save_deposit_products(request):
    response = requests.get(URL).json()
    
    
    print(response)
    
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

@api_view(['GET'])
def deposit_list(request):
    deposits = Deposit.objects.all()
    serializer = DepositSerializer(deposits, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def depositOption_list(request, deposit_code):
    deposit = get_object_or_404(Deposit, deposit_code=deposit_code)
    deposit_options = DepositOption.objects.filter(deposit=deposit)

    if request.method == 'GET':
        serializer = DepositOptionSerializer(deposit_options, many=True)
        return Response(serializer.data)