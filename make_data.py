# make_data.py 파일은 랜덤한 더미 데이터를 만드는 예시 파일입니다.
# 반드시, 사용하는 필드를 확인한 후 본인의 프로젝트에 맞게 수정하여 진행해야 합니다.

# [참고] 현재 코드는 아래 User 모델을 기준으로 작성되어 있습니다.
"""
class User(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    money = models.IntegerField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    # 가입한 상품 목록 리스트를 ,로 구분된 문자열로 저장함
    financial_products = models.TextField(blank=True, null=True)

    # superuser fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
"""


import random
import requests
import os

first_name_samples = '김이박최정강조윤장임'
middle_name_samples = '민서예지도하주윤채현지'
last_name_samples = '준윤우원호후서연아은진'


def random_name():
    result = ''
    result += random.choice(first_name_samples)
    result += random.choice(middle_name_samples)
    result += random.choice(last_name_samples)
    return result + str(random.randint(1, 100))


# 현재 API 에 들어있는 금융 상품 코드 리스트 저장
DP_URL = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
SP_URL = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'

API_KEY = '05123616ac0af1b386553f893c720f21'

financial_products = []

params = {
    'auth': API_KEY,
    # 금융회사 코드 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
    'topFinGrpNo': '020000',
    'pageNo': 1,
}


# 정기예금 목록 저장
response = requests.get(DP_URL, params=params).json()
baseList = response.get('result').get('baseList')  # 상품 목록

for product in baseList:
    financial_products.append(product['fin_prdt_cd'])

# 적금 목록 저장
response = requests.get(SP_URL, params=params).json()
baseList = response.get('result').get('baseList')  # 상품 목록

for product in baseList:
    financial_products.append(product['fin_prdt_cd'])

dict_keys = [
    'username',
    'name',
    'email',
    'profile_img',
    'financial_products',
    'age',
    'money',
    'salary',
    'desire_amount_saving',
    'desire_amount_deposit',
    'deposit_period',
    'saving_period',
]

# json 파일 만들기
import json
from collections import OrderedDict

file = OrderedDict()

username_list = []
N = 10000
i = 0

while i < N:
    rn = random_name()
    if rn in username_list:
        continue

    username_list.append(rn)
    i += 1

# 저장 위치는 프로젝트 구조에 맞게 수정합니다.
save_dir = '../GSCH_back/accounts/fixtures/accounts/user_data.json'

# 디렉토리가 없는 경우 생성
os.makedirs(os.path.dirname(save_dir), exist_ok=True)

with open(save_dir, 'w', encoding="utf-8") as f:
    # 이하 코드는 동일...

    for i in range(N):
        # 랜덤한 데이터를 삽입
        file['model'] = 'accounts.User'
        file['pk'] = i + 1
        file['fields'] = {
            'username': username_list[i],  # 유저 이름 랜덤 생성
            'name': random_name(),  # 이름 랜덤 생성
            'email': f'user{i}@example.com',  # 이메일 생성
            'profile_img': 'image/user.png',  # 프로필 이미지
            'financial_products': ','.join(
                [
                    random.choice(financial_products)
                    for _ in range(random.randint(0, 5))
                ]
            ),  # 금융 상품 리스트
            'age': random.randint(1, 100),  # 나이
            'money': random.randrange(0, 100000000, 100000),  # 현재 가진 금액
            'salary': random.randrange(0, 1500000000, 1000000),  # 연봉
            'desire_amount_saving': random.randrange(0, 500000000, 100000),  # 희망 적금 금액
            'desire_amount_deposit': random.randrange(0, 500000000, 100000),  # 희망 예금 금액
            'deposit_period': random.randint(1, 60),  # 예금 기간 (개월)
            'saving_period': random.randint(1, 60),  # 적금 기간 (개월)
            'is_superuser': False,
        }

        json.dump(file, f, ensure_ascii=False, indent='\t')
        if i != N - 1:
            f.write(',')
    f.write(']')
    f.close()

print(f'데이터 생성 완료 / 저장 위치: {save_dir}')