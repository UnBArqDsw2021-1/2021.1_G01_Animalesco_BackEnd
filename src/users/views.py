from django.contrib.auth import logout
from django.core.exceptions import ImproperlyConfigured

from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response


from .models import User
from .utils import get_and_authenticate_user
from . import serializers


class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny,]
    serializer_class = serializers.EmptySerializer

    serializer_classes = {
        'login': serializers.UserSignInSerializer,
        'register': serializers.UserSignUpSerializer,
        'password_change': serializers.PasswordChangeSerializer,
    }

    def get_serializer_class(self):
        """
        Normalmente as uma viewset possui somente um serializador.
        Porém, para essa model viewset queremos serializadores diferentes de acordo com o
        método que será executado, dessa forma, essa função retorna o serializador correto
        de acordo com o contexto da requisição.
        """

        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]

        return super().get_serializer_class()

    @action(methods=['POST'], detail=False)
    def login(self, request):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        user = get_and_authenticate_user(**validated_data)

        data = serializers.LoggedUserSerializer(user).data
        return Response(data=data, status=status.HTTP_200_OK)


    @action(methods=['POST', ], detail=False)
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        validated_data.pop('password_confirmation')
        print("validated_data")
        print(validated_data)
        user = User.objects.create_user(**validated_data)

        data = serializers.LoggedUserSerializer(user).data
        return Response(data=data, status=status.HTTP_201_CREATED)

    @action(methods=['POST', ], detail=False)
    def logout(self, request):
        logout(request)
        data = {'message': 'Sucessfully logged out'}
        return Response(data=data, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=False, permission_classes=[IsAuthenticated, ])
    def password_change(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        request.user.set_password(validated_data['new_password'])
        request.user.save()
        data = {"message": "Password modified successfully"}
        return Response(data, status=status.HTTP_200_OK)
