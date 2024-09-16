from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

CustomUser = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the CustomUser model.
    """
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'bio', 'profile_picture')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Create a new user instance.
        """
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', '')
        )
        return user

class TokenSerializer(serializers.ModelSerializer):
    """
    Serializer for the Token model.
    """
    token = serializers.CharField()

    class Meta:
        model = Token
        fields = ('key',)

    def create(self, validated_data):
        """
        Create a new token instance.
        """
        token = Token.objects.create(user=self.context['request'].user)
        return token