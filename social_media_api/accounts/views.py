from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, TokenSerializer
from .models import CustomUser

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = CustomUser.objects.create_user(**serializer.validated_data)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response(serializer.errors, status=400)

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'User not found'}, status=404)

class TokenRetrieveView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            token, created = Token.objects.get_or_create(user=request.user)
            serializer = TokenSerializer(token)
            return Response(serializer.data)
        return Response({'error': 'User not authenticated'}, status=401)