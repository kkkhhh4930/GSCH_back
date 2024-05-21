from rest_framework import serializers
from .models import User
from financial.serializers import DepositSerializer, SavingSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer

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

class CustomRegisterSerializer(RegisterSerializer):

    name = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=50
        )


    def get_cleaned_data(self):
        # print(self.validated_data)
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'name': self.validated_data.get('name', ''),
            'email': self.validated_data.get('email', ''),
        }
