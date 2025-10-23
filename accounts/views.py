from django.contrib.auth import authenticate, get_user_model
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import json

from .models import User, Course
from .serializers import UserSerializer, CourseSerializer

User = get_user_model()


# --- Course ViewSet (from your friend’s code) ---
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# --- User CRUD (optional, DRF API) ---
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# --- User Registration ---
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    try:
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        role = data.get('role', 'student')

        if User.objects.filter(username=username).exists():
            return Response({'message': 'Username already exists'}, status=400)

        user = User.objects.create_user(
            username=username, email=email, password=password, role=role
        )

        return Response({
            'message': 'User registered successfully',
            'username': user.username,
            'role': user.role
        }, status=201)
    except Exception as e:
        return Response({'message': f'Error: {str(e)}'}, status=500)


# --- User Login ---
@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            return Response({
                'message': 'Login successful',
                'user_id': user.id,
                'username': user.username,
                'role': user.role
            }, status=200)
        else:
            return Response({'message': 'Invalid username or password'}, status=401)
    except Exception as e:
        return Response({'message': f'Error: {str(e)}'}, status=500)
