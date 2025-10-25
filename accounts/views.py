    from rest_framework.authtoken.models import Token

    @api_view(['POST'])
    @permission_classes([AllowAny])
    def login_user(request):
        data = request.data
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            # Create or get token
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'message': 'Login successful',
                'token': token.key,
                'user_id': user.id,
                'username': user.username,
                'role': getattr(user, 'role', None),
            }, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
