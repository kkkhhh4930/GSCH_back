from rest_framework import serializers
from .models import Deposit, DepositOption
from .models import Saving, SavingOption

class DepositOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOption
        fields = '__all__'
        read_only_fields = ('deposit',)

class SavingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOption
        fields = '__all__'
        read_only_fields = ('saving',)

class DepositSerializer(serializers.ModelSerializer):
    depositoption_set = DepositOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Deposit
        fields = '__all__'
        read_only_fields = ('contract_user',)


class SavingSerializer(serializers.ModelSerializer):
    savingoption_set = SavingOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Saving
        fields = '__all__'
        read_only_fields = ('contract_user',)


# class ContractDepositSerializer(serializers.ModelSerializer):
#     depositoption_set = DepositOptionSerializer(many=True, read_only=True)
#     class Meta:
#         model = Deposit
#         fields = ('deposit_code','name', 'kor_co_nm', 'depositoption_set')


# class ContractSavingSerializer(serializers.ModelSerializer):
#     savingoption_set = SavingOptionSerializer(many=True, read_only=True)
#     class Meta:
#         model = Saving
#         fields = ('saving_code','name','kor_co_nm', 'savingoption_set')