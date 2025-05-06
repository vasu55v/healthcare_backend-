from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'password']
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    tokens = serializers.SerializerMethodField()
    
    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])
        refresh = RefreshToken.for_user(user)
        
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
    
    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        
        if email is None:
            raise serializers.ValidationError('An email address is required to log in.')
        
        if password is None:
            raise serializers.ValidationError('A password is required to log in.')
        
        user = authenticate(username=email, password=password)
        
        if user is None:
            raise serializers.ValidationError('A user with this email and password was not found.')
        
        if not user.is_active:
            raise serializers.ValidationError('This user has been deactivated.')
        
        return {
            'email': user.email,
            'name': user.name
        }