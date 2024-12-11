from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password2 = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    cedula = serializers.CharField(max_length=15, required=True)  # Nuevo campo para la cédula

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password2', 'cedula')

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already exists")
        return email

    def validate_password2(self, password2):
        password1 = self.initial_data.get("password")
        if password1 and password2 and password1 != password2:
            raise serializers.ValidationError("Passwords mismatched")
        return password2

    def create(self, validated_data):
        # Eliminar 'password2' del validated_data antes de usarlo para crear el usuario
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')

        instance = User.objects.create(**validated_data)
        instance.set_password(password)  # Cifra la contraseña
        instance.save()
        return instance
