from django.core import exceptions
from django.core.exceptions import ValidationError
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import BaseUserManager
import django.contrib.auth.password_validation as validators
from rest_framework.authtoken.models import Token

from .models import User


class UserSignInSerializer(serializers.Serializer):
    """
    Informações necessárias para fazer login
    """
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)


class LoggedUserSerializer(serializers.ModelSerializer):
    """
    Informações que são retornadas quando o usuário realiza o login com sucesso.
    """
    auth_token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'auth_token')

    def get_auth_token(self, obj):
        token, created = Token.objects.get_or_create(user=obj)
        return token.key
        # @Bc129865

class UserSignUpSerializer(serializers.ModelSerializer):
    """
    Informações que são recebidas quando é necessário criar um usuário
    """

    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password_confirmation = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirmation', 'first_name',
                  'last_name')

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already taken")

        # Método builtin do django que normaliza emails
        return BaseUserManager.normalize_email(value)

    def validate(self, data):
        password = data.get('password')
        password_confirmation = data.get('password_confirmation')

        user = User(
            username = data.get('username'),
            email = data.get('email'),
            first_name = data.get('first_name'),
            last_name = data.get('last_name'),
        )

        if password != password_confirmation:
            raise ValidationError("Passwords must match")

        errors = dict()

        try:
            validators.validate_password(password=password, user=user)

        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return super().validate(data)


class PasswordChangeSerializer(serializers.Serializer):

    current_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    new_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    new_password_confirmation = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
    )

    def validate_current_password(self, value):
        request = self.context.get('request')
        user = request.user

        if user.check_password(value):
            raise serializers.ValidationError('Current passwotd does not match')

        return value

    def validate(self, data):
        new_password = data.get('new_password')
        new_password_confirmation = data.get('new_password_confirmation')

        if new_password != new_password_confirmation:
            raise ValidationError("Passwords must match")

        errors = dict()
        request = self.context.get('request')
        user = request.user

        try:
            validators.validate_password(password=new_password, user=user)

        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return super().validate(data)


class EmptySerializer(serializers.Serializer):
    pass