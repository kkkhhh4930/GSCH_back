from rest_framework import serializers
from .models import User
from financial.serializers import DepositSerializer, SavingSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('profile_img', 'id', 'username', 'name', 'email', 'age', 'money', 'salary')
        read_only_fields = ('id','username', 'name',)
class UserInfoSerializer(serializers.ModelSerializer):
        profile_img = serializers.ImageField(use_url=True)
        contract_deposit = DepositSerializer(many=True)
        contract_saving = SavingSerializer(many=True)
        class Meta:
            model = User
            fields = '__all__'
            read_only_fields = ('id','username', 'name',)