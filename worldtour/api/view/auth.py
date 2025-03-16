from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.decorators import api_view
from user.models import User
from ..serializers import UserSerializer

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access.token),
    }

@api_view(['POST'])
def register_user(request):
    userName = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    if not userName or not email or not password:
        return JsonResponse({'error':'Please provide all the fields'},status=status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(username=userName).exists():
        return JsonResponse({'error':'Username already exists'},status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create(username=userName,email=email,password=password)
    return JsonResponse(get_tokens_for_user(user),status=status.HTTP_201_CREATED)


@api_view(['POST'])
def login_user(request):
    from django.contrib.auth import authenticate

    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        tokens = get_tokens_for_user(user)
        return JsonResponse(tokens)
    else:
        return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()
    serilizer = UserSerializer(users,many=True)
    return JsonResponse({'users':serilizer.data},status=status.HTTP_200_OK)