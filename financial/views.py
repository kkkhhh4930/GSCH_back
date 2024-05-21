import requests
from .models import Deposit, DepositOption, Saving, SavingOption
from .serializers import DepositSerializer, DepositOptionSerializer, SavingSerializer, SavingOptionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

API_KEY = '05123616ac0af1b386553f893c720f21'


@api_view(['POST'])
def save_deposit_products(request):
    DEPOSIT_API_URL = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(DEPOSIT_API_URL).json()
    base_list = response.get('result').get('baseList')
    option_list = response.get('result').get('optionList')

    for base in base_list:
        if Deposit.objects.filter(fin_prdt_cd=base.get('fin_prdt_cd')).exists():
            continue
        save_product = {
            'fin_prdt_cd': base.get('fin_prdt_cd', '-1'),
            'fin_co_no': base.get('fin_co_no', '-1'),
            'kor_co_nm': base.get('kor_co_nm', '-1'),
            'fin_prdt_nm': base.get('fin_prdt_nm', '-1'),
            'dcls_month': base.get('dcls_month', '-1'),
            'mtrt_int': base.get('mtrt_int', '-1'),
            'etc_note': base.get('etc_note', '-1'),
            'join_deny': base.get('join_deny', -1),
            'join_member': base.get('join_member', '-1'),
            'join_way': base.get('join_way', '-1'),
            'spcl_cnd': base.get('spcl_cnd', '-1'),
            'max_limit': base.get('max_limit', -1),
        }
        serializer = DepositSerializer(data=save_product)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    for option in option_list:
        prdt_cd = option.get('fin_prdt_cd', '-1')
        product = Deposit.objects.get(fin_prdt_cd=prdt_cd)
        save_option = {
            'intr_rate_type_nm': option.get('intr_rate_type_nm', '-1'),
            'intr_rate': option.get('intr_rate', -1),
            'intr_rate2': option.get('intr_rate2', -1),
            'save_trm': option.get('save_trm', -1),
        }
        serializer = DepositOptionSerializer(data=save_option)
        if serializer.is_valid(raise_exception=True):
            serializer.save(deposit=product)

    return Response({"status": "success", "message": "Deposit products saved successfully."})


@api_view(['POST'])
def save_saving_products(request):
    SAVING_API_URL = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(SAVING_API_URL).json()
    base_list = response.get('result').get('baseList')
    option_list = response.get('result').get('optionList')

    for base in base_list:
        if Saving.objects.filter(fin_prdt_cd=base.get('fin_prdt_cd')).exists():
            continue
        save_product = {
            'fin_prdt_cd': base.get('fin_prdt_cd', '-1'),
            'fin_co_no': base.get('fin_co_no', '-1'),
            'kor_co_nm': base.get('kor_co_nm', '-1'),
            'fin_prdt_nm': base.get('fin_prdt_nm', '-1'),
            'dcls_month': base.get('dcls_month', '-1'),
            'mtrt_int': base.get('mtrt_int', '-1'),
            'etc_note': base.get('etc_note', '-1'),
            'join_deny': base.get('join_deny', -1),
            'join_member': base.get('join_member', '-1'),
            'join_way': base.get('join_way', '-1'),
            'spcl_cnd': base.get('spcl_cnd', '-1'),
            'max_limit': base.get('max_limit', -1),
        }
        serializer = SavingSerializer(data=save_product)
        if serializer.is_valid(raise_exception=True):
            product = serializer.save()

    for option in option_list:
        prdt_cd = option.get('fin_prdt_cd', '-1')
        product = Saving.objects.get(fin_prdt_cd=prdt_cd)
        save_option = {
            'intr_rate_type_nm': option.get('intr_rate_type_nm', '-1'),
            'rsrv_type_nm': option.get('rsrv_type_nm', '-1'),
            'intr_rate': option.get('intr_rate', -1),
            'intr_rate2': option.get('intr_rate2', -1),
            'save_trm': option.get('save_trm', -1),
        }
        serializer = SavingOptionSerializer(data=save_option)
        if serializer.is_valid(raise_exception=True):
            serializer.save(saving=product)

    return Response({"status": "success", "message": "Saving products saved successfully."})





@api_view(['GET'])
def deposit_list(request):
    deposits = Deposit.objects.all()
    serializer = DepositSerializer(deposits, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def deposit_detail(request, deposit_code):
    deposit = get_object_or_404(Deposit, fin_prdt_cd=deposit_code)
    serializer = DepositSerializer(deposit)
    return Response(serializer.data)


@api_view(['GET'])
def deposit_option_list(request, deposit_code):
    deposit = get_object_or_404(Deposit, fin_prdt_cd=deposit_code)
    deposit_options = DepositOption.objects.filter(deposit=deposit)
    serializer = DepositOptionSerializer(deposit_options, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def deposit_option_detail(request, deposit_code, deposit_option_pk):
    deposit = get_object_or_404(Deposit, fin_prdt_cd=deposit_code)
    deposit_option = get_object_or_404(DepositOption, pk=deposit_option_pk, deposit=deposit)
    serializer = DepositOptionSerializer(deposit_option)
    return Response(serializer.data)


@api_view(['GET'])
def saving_list(request):
    savings = Saving.objects.all()
    serializer = SavingSerializer(savings, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def saving_detail(request, saving_code):
    saving = get_object_or_404(Saving, fin_prdt_cd=saving_code)
    serializer = SavingSerializer(saving)
    return Response(serializer.data)

@api_view(['GET'])
def saving_option_list(request, saving_code):
    saving = get_object_or_404(Saving, fin_prdt_cd=saving_code)
    saving_options = SavingOption.objects.filter(saving=saving)
    serializer = SavingOptionSerializer(saving_options, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def saving_option_detail(request, saving_code, saving_option_pk):
    saving = get_object_or_404(Saving, fin_prdt_cd=saving_code)
    saving_option = get_object_or_404(SavingOption, pk=saving_option_pk, saving=saving)
    serializer = SavingOptionSerializer(saving_option)
    return Response(serializer.data)
