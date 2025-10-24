from django.contrib.auth import authenticate, get_user_model, login, logout
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import User, Course
from .serializers import UserSerializer, CourseSerializer

User = get_user_model()


# -------------------------------
# Course ViewSet
# -------------------------------
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# -------------------------------
# User ViewSet (optional)
# -------------------------------
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# -------------------------------
# User Registration
# -------------------------------
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    data = request.data
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role', 'student')

    if User.objects.filter(username=username).exists():
        return Response({'message': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, email=email, password=password, role=role)
    return Response({
        'message': 'User registered successfully',
        'username': user.username,
        'role': user.role
    }, status=status.HTTP_201_CREATED)


# -------------------------------
# User Login
# -------------------------------
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    data = request.data
    username = data.get('username')
    password = data.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)  # <-- this sets the session
        return Response({
            'message': 'Login successful',
            'user_id': user.id,
            'username': user.username,
            'role': getattr(user, 'role', None),
        }, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)


# -------------------------------
# User Logout
# -------------------------------
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    logout(request)
    return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)


# -------------------------------
# User Profile (for React frontend)
# -------------------------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    return Response({
        'user_id': user.id,
        'username': user.username,
        'email': user.email,
        'role': getattr(user, 'role', None),
    })
