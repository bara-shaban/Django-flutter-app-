from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import CustomUserRegistrationSerializer, CustomUserDeleteSerializer
from rest_framework import permissions, status
from rest_framework.response import Response


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
        print("Request data:", request.data)
        print("Request user:", request.user)
        print("Authenticated:", request.user.is_authenticated)
        print("Request method:", request.method)
        print(
            "Permissions:",
            [perm.__class__.__name__ for perm in self.permission_classes],
        )

        email = request.data["email"]
        if not email:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = CustomUserDeleteSerializer(data={"email": email})

        try:
            is_valid = serializer.is_valid()
            print("serializer is valid:", is_valid)

            print("serializer errors:", serializer.errors)

            return Response(
                status=status.HTTP_204_NO_CONTENT,
            )
        except Exception as e:
            print("Exception:", e)
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
            )
