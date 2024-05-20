from django.db import models
from django.conf import settings


class Deposit(models.Model):
    fin_prdt_cd = models.TextField(unique=True, null = True)    # 금융 상품 코드
    kor_co_nm = models.TextField(null = True)                   # 금융회사명
    fin_prdt_nm = models.TextField(null = True)                 # 금융 상품명
    etc_note = models.TextField(null = True)                    # 금융 상품 설명
    join_deny = models.IntegerField(null = True)                # 가입 제한
    join_member = models.TextField(null = True)                 # 가입대상
    join_way = models.TextField(null = True)                    # 가입 방법
    spcl_cnd = models.TextField(null = True)                    # 우대조건
    dcls_month = models.CharField(max_length=20)                # 공시 제출월


class DepositOption(models.Model):
    deposit = models.ForeignKey(Deposit, on_delete = models.CASCADE)
    fin_prdt_cd = models.TextField()                            # 금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length=100)        # 저축금리 유형명
    intr_rate = models.FloatField(blank=True, default=-1)       # 저축금리
    intr_rate2 = models.FloatField(blank=True, default=-1)      # 최고우대금리
    save_trm = models.IntegerField()                            # 저축기간 (단위 : 개월)


class Saving(models.Model):
    fin_prdt_cd = models.TextField(unique=True, null = True)    # 금융 상품 코드
    kor_co_nm = models.TextField(null = True)                   # 금융회사명
    fin_prdt_nm = models.TextField(null = True)                 # 금융 상품명
    etc_note = models.TextField(null = True)                    # 금융 상품 설명
    join_deny = models.IntegerField(null = True)                # 가입 제한
    join_member = models.TextField(null = True)                 # 가입대상
    join_way = models.TextField(null = True)                    # 가입 방법
    spcl_cnd = models.TextField(null = True)                    # 우대조건
    dcls_month = models.CharField(max_length=20)                # 공시 제출월

class SavingOption(models.Model):
    saving = models.ForeignKey(Saving, on_delete = models.CASCADE)
    fin_prdt_cd = models.TextField()                            # 금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length=100)        # 저축금리 유형명
    intr_rate = models.FloatField(blank=True, default=-1)       # 저축금리
    intr_rate2 = models.FloatField(blank=True, default=-1)      # 최고우대금리
    save_trm = models.IntegerField()                            # 저축기간 (단위 : 개월)