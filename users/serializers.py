from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password
from .models import CustomUser
from django.core.files.storage import FileSystemStorage
import os

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'email', 'first_name', 'last_name', 'role',
            'profile_image', 'phone_number', 'is_active'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'is_active': {'read_only': True},
            'date_joined': {'read_only': True}
        }

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def validate_phone_number(self, value):
        if len(value) < 10:
            raise serializers.ValidationError(
                "Phone number must be at least 10 digits"
            )
        return value

    def validate_role(self, value):
        valid_roles = ['customer', 'hotel']
        if value not in valid_roles:
            raise serializers.ValidationError(
                f"Role must be one of {valid_roles}"
            )
        return value

    def validate_profile_image(self, value):
        if value:
            max_size = 1024 * 1024   
            if value.size > max_size:
                raise serializers.ValidationError(
                    "Profile image size must be less than 1MB"
                )
        return value

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        token = self.get_token(self.user)
        
        data['user_data'] = {
            'email': self.user.email,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'role': self.user.role,
            'phone_number': self.user.phone_number,
            'profile_image': str(self.user.profile_image.url) if self.user.profile_image else None,
            'date_joined': self.user.date_joined.isoformat()
        }
        
        return data
    


# from rest_framework import serializers

# from models import CustomUser

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = [
#             'id', 'email', 'first_name', 'last_name', 'role', 'profile_image', 'phone_number', 'date_joined'
#         ]

#         read_only_fields = ['id', 'email', 'date_joined']


# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = CustomUser
#         fields = [
#             'email', 'password', 'first_name', 'last_name',
#             'role', 'profile_image', 'phone_number'
#         ]

#     def create(self, validated_data):
#         user = CustomUser.objects.create_user(
#             email=validated_data['email'],
#             password=validated_data['password'],
#             first_name=validated_data.get('first_name', ''),
#             last_name=validated_data.get('last_name', ''),
#             role=validated_data.get('role', 'customer'),
#             profile_image=validated_data.get('profile_image'),
#             phone_number=validated_data.get('phone_number'),
#         )
#         return user