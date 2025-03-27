from rest_framework import serializers, validators
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model


class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[
            validators.UniqueValidator(
                queryset=get_user_model().objects.all(),
            ),
        ],
    )
    password = serializers.CharField(
        min_length=8,
        write_only=True,
        validators=[validate_password],
        style={
            "input_type": "password",
        },
    )
    confirm_password = serializers.CharField(
        min_length=8,
        write_only=True,
        style={
            "input_type": "password",
        },
    )

    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "password",
            "confirm_password",
        )

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        user = get_user_model().objects.create(
            email=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class CustomUserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["email"]
        extra_kwargs = {
            "email": {
                "validators": [],
            },
        }

    def validate(self, attrs):
        email = attrs["email"]
        if not get_user_model().objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {"email": "User with this email does not exist."}
            )
        return attrs
