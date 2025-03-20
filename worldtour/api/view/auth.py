from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access.token),
    }


@api_view(["POST"])
def register_user(request):
    try:
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")
        if not username or not password or not email:
            return JsonResponse(
                {"error": "Please provide all the fields"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if User.objects.filter(username=username).exists():
            return JsonResponse(
                {"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST
            )
        user = User.objects.create_user(
            username=username, email=email, password=password
        )
        user.save()
        tokens = get_tokens_for_user(user)
        return JsonResponse(tokens, status=status.HTTP_201_CREATED)
    except Exception as e:
        return JsonResponse(
            {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(["POST"])
def login_user(request):

    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user is not None:
        tokens = get_tokens_for_user(user)
        return JsonResponse(tokens)
    else:
        return JsonResponse(
            {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


""" @api_view(["GET"])
def get_all_users(request):
    users = User.objects.all()
    serilizer = UserSerializer(users, many=True)
    return JsonResponse({"users": serilizer.data}, status=status.HTTP_200_OK) """


@api_view(["DELETE"])
def delete_user(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        return JsonResponse(
            {"message": "User deleted successfully"}, status=status.HTTP_200_OK
        )
    except User.DoesNotExist:
        return JsonResponse(
            {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return JsonResponse(
            {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
