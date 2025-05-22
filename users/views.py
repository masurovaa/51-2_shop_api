from rest_framework.decorators import api_view
from users.serializers import (UserCreateSerializer, UserAuthSerializer)
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import VerificationCode
import random


@api_view(['POST'])
def registration_api_view(request):
    serilizer = UserCreateSerializer(data=request.data)
    serilizer.is_valid(raise_exception=True)
    username = serilizer.validated_data['username']
    password = serilizer.validated_data['password']
    user = User.objects.create_user(username=username, password=password, is_active=False)
    VerificationCode.objects.create(user=user)
    code = str(random.randint(100000, 999999))
    return Response(status=status.HTTP_201_CREATED, data={'user_id': user.id,
    'message': 'User created. Please confirm your account with the code sent.'})


@api_view(['POST'])
def authorization_api_view(request):
    serializer = UserAuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(**serializer.validated_data) # object / None
    if user:
        if not user.is_active:
            return Response({'detail': 'User is not active. Please confirm your account.'},
                            status=status.HTTP_403_FORBIDDEN)
        token, created = Token.objects.get_or_create(user=user)
        return Response(data={'key': token.key})
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def confirm_api_view(request):
    serializer = UserConfirmSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data['username']
    code = serializer.validated_data['code']

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    if user.is_active:
        return Response({'message': 'User already active'}, status=status.HTTP_400_BAD_REQUEST)

    if user.verification_code.code == code:
        user.is_active = True
        user.save()
        user.verification_code.delete()
        return Response({'message': 'User confirmed successfully'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid confirmation code'}, status=status.HTTP_400_BAD_REQUEST)