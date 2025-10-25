# accounts/views.py

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer

User = get_user_model()

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    """
    Handles user registration.
    - Checks if the username or email already exists.
    - Creates the user if validation passes.
    """
    email = request.data.get('email')
    username = request.data.get('username')
    password = request.data.get('password')

    # Check if all fields are provided
    if not email or not username or not password:
        return Response({"message": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

    # Check if email or username already exists
    if User.objects.filter(email=email).exists():
        return Response({"message": "Email already exists."}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({"message": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

    # Proceed with user creation
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        user.set_password(password)  # Ensure password is hashed
        user.save()

        # Create the token for the user
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            'message': 'User registered successfully',
            'token': token.key,
            'username': user.username,
            'role': user.role,
            'email': user.email,
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    """
    Handles user login.
    - Authenticates the user based on username and password.
    - Returns a token if login is successful.
    """
    username = request.data.get('username')
    password = request.data.get('password')

    # Authenticate the user
    user = authenticate(username=username, password=password)

    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'message': 'Login successful',
            'token': token.key,
            'user_id': user.id,
            'username': user.username,
            'role': getattr(user, 'role', None),  # Return role if defined in User model
        }, status=status.HTTP_200_OK)

    return Response({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
