from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import CustomUserRegistrationSerializer, CustomUserDeleteSerializer
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class CustomUserRegister(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = CustomUserRegistrationSerializer
    permission_classes = [
        permissions.AllowAny,
    ]

    def create(self, request, *args, **kwargs):
        try:
            super().create(request, *args, **kwargs)
            return Response(
                status=status.HTTP_201_CREATED,
            )
        except:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
            )


class CustomUserDelete(generics.DestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserDeleteSerializer
    permission_classes = [
        permissions.AllowAny,
    ]

    def destroy(self, request, *args, **kwargs):
        email = request.data["email"]
        if not email:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = CustomUserDeleteSerializer(data={"email": email})

        try:
            is_valid = serializer.is_valid(raise_exception=True)
            if is_valid:
                user = get_user_model().objects.get(email=email)
                user.delete()

            return Response(
                status=status.HTTP_204_NO_CONTENT,
            )
        except Exception as e:
            print("Exception:", e)
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
            )


class GetCustomUser(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        return Response(
            {
                "email": user.email,
                "is_staff": user.is_staff,
                "is_superuser": user.is_superuser,
            }
        )
