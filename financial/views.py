import requests
import pandas as pd
from .models import Deposit, DepositOption, Saving, SavingOption
from accounts.models import User
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
deposit_URL= f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
saving_URL= f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'

@api_view(['GET'])
def save_deposit_products(request):
    response = requests.get(deposit_URL).json()
    
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
        dcls_month = li.get('dcls_month')
        
    
            
        save_data = {
            'fin_prdt_cd' : fin_prdt_cd,
            'kor_co_nm' : kor_co_nm,
            'fin_prdt_nm' : fin_prdt_nm,
            'etc_note' : etc_note,
            'join_deny' : join_deny,
            'join_member' : join_member,
            'join_way' : join_way,
            'spcl_cnd' : spcl_cnd,
            'dcls_month' : dcls_month,
        }
        if Deposit.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
            Deposit.objects.filter(fin_prdt_cd=fin_prdt_cd).delete()
            
        serializer = DepositSerializer(data = save_data)
        
        # 유효성 검증
        if serializer.is_valid(raise_exception=True):
            # 유효하다면 저장
            serializer.save()

    for option in response.get('result').get('optionList'):
        deposit = Deposit.objects.get(fin_prdt_cd=option.get('fin_prdt_cd'))
        option_save_data = {
        'fin_prdt_cd': option.get('fin_prdt_cd'),
        'intr_rate_type_nm': option.get('intr_rate_type_nm'),
        'intr_rate': option.get('intr_rate'),
        'intr_rate2': option.get('intr_rate2'),
        'save_trm': option.get('save_trm'),
        }

        optionserializer = DepositOptionSerializer(data=option_save_data)

        if optionserializer.is_valid(raise_exception=True):
            optionserializer.save(deposit=deposit)

    return JsonResponse({'message': 'Data saved successfully'})

@api_view(['GET'])
def save_saving_products(request):
    response = requests.get(saving_URL).json()
    
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
        dcls_month = li.get('dcls_month')
    
            
        save_data = {
            'fin_prdt_cd' : fin_prdt_cd,
            'kor_co_nm' : kor_co_nm,
            'fin_prdt_nm' : fin_prdt_nm,
            'etc_note' : etc_note,
            'join_deny' : join_deny,
            'join_member' : join_member,
            'join_way' : join_way,
            'spcl_cnd' : spcl_cnd,
            'dcls_month' : dcls_month,
        }
        if Saving.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
            Saving.objects.filter(fin_prdt_cd=fin_prdt_cd).delete()
            
        serializer = SavingSerializer(data = save_data)
        
        # 유효성 검증
        if serializer.is_valid(raise_exception=True):
            # 유효하다면 저장
            serializer.save()

    for option in response.get('result').get('optionList'):
        saving = Saving.objects.get(fin_prdt_cd=option.get('fin_prdt_cd'))
        option_save_data = {
        'fin_prdt_cd': option.get('fin_prdt_cd'),
        'intr_rate_type_nm': option.get('intr_rate_type_nm'),
        'intr_rate': option.get('intr_rate'),
        'intr_rate2': option.get('intr_rate2'),
        'save_trm': option.get('save_trm'),
        }

        optionserializer = SavingOptionSerializer(data=option_save_data)

        if optionserializer.is_valid(raise_exception=True):
            optionserializer.save(saving=saving)

    return JsonResponse({'message': 'Data saved successfully'})

@api_view(['GET'])
def deposit_list(request):
    deposits = Deposit.objects.all()
    serializer = DepositSerializer(deposits, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def saving_list(request):
    savings = Saving.objects.all()
    serializer = SavingSerializer(savings, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def deposit_detail(request, fin_prdt_cd):
    deposit = get_object_or_404(Deposit, fin_prdt_cd=fin_prdt_cd)
    if request.method == 'GET':
        serializer = DepositSerializer(deposit)
        return Response(serializer.data) 

@api_view(['GET'])
def depositOption_list(request, fin_prdt_cd):
    deposit = get_object_or_404(Deposit, fin_prdt_cd=fin_prdt_cd)
    deposit_options = DepositOption.objects.filter(deposit=deposit)

    if request.method == 'GET':
        serializer = DepositOptionSerializer(deposit_options, many=True)
        return Response(serializer.data)














@api_view(['GET'])
def depositOption_list(request, deposit_code):
    deposit = get_object_or_404(Deposit, deposit_code=deposit_code)
    deposit_options = DepositOption.objects.filter(deposit=deposit)

    if request.method == 'GET':
        serializer = DepositOptionSerializer(deposit_options, many=True)
        return Response(serializer.data)


# # 1. 데이터 불러오기 및 전처리
    
# def get_user_data():
#     users = User.objects.all().values()
#     df = pd.DataFrame(users)
#     return df
# user_data = get_user_data()


# # 2. 비슷한 사용자 찾기
# def find_similar_users(user_data, target_user_id, age_threshold=5, money_threshold=5000000, top_n=100):
#     target_user = user_data[user_data['id'] == target_user_id].iloc[0]
#     similar_users = user_data[
#         (user_data['age'].between(target_user['age'] - age_threshold, target_user['age'] + age_threshold)) &
#         (user_data['money'].between(target_user['money'] - money_threshold, target_user['money'] + money_threshold))
#     ]
#     return similar_users.head(top_n)


# # 3. 금융 상품 데이터 가져오기
# def get_financial_products(api_key):
#     DP_URL = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
#     SP_URL = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'

#     params = {
#         'auth': api_key,
#         'topFinGrpNo': '020000',
#         'pageNo': 1,
#     }

#     # 정기예금 목록 저장
#     response = requests.get(DP_URL, params=params).json()
#     deposit_products = response.get('result').get('baseList')

#     # 적금 목록 저장
#     response = requests.get(SP_URL, params=params).json()
#     saving_products = response.get('result').get('baseList')

#     financial_products = deposit_products + saving_products

#     # DataFrame으로 변환
#     products_df = pd.DataFrame(financial_products)
#     return products_df

# api_key = '05123616ac0af1b386553f893c720f21'
# products_df = get_financial_products(api_key)

# # 4. 상품 추천
# def recommend_products(similar_users, products_df, top_n=10):
#     product_list = []
    
#     for products in similar_users['financial_products']:
#         if products:
#             product_list.extend(products.split(','))

#     product_series = pd.Series(product_list)
#     top_products = product_series.value_counts().head(top_n).index.tolist()

#     recommended_products = products_df[products_df['fin_prdt_cd'].isin(top_products)]
#     recommended_products_sorted = recommended_products.sort_values(by='intr_rate', ascending=False)

#     return recommended_products_sorted.head(top_n)

# # 특정 사용자 ID로 유사 사용자 찾기 및 상품 추천
# target_user_id = 1  # 예시로 1번 사용자
# similar_users = find_similar_users(user_data, target_user_id)
# recommended_products = recommend_products(similar_users, products_df)
# print(recommended_products[['fin_prdt_nm', 'intr_rate']])