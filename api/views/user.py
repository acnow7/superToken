from rest_framework.response import Response
from rest_framework import status, generics
from ..serializers.user import UserSerializer
from ..serializers.ChangePasswordSerializer import ChangePasswordSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token

class SignUp(generics.CreateAPIView):
        # Override the authentication/permissions classes so this endpoint
        # is not authenticated & we don't need any permissions to access it.
        authentication_classes = ()
        permission_classes = ()

        def post(self, request):
            new_user = UserSerializer(data=request.data)
            if new_user.is_valid():
                  # Save the user and send back a response!
                new_user.save()
                return Response({ 'user': new_user.data }, status=status.HTTP_201_CREATED)
            else:
                return Response(new_user.errors, status=status.HTTP_400_BAD_REQUEST) 


class SignIn(generics.CreateAPIView):
    # Override the authentication/permissions classes so this endpoint
    # is not authenticated & we don't need any permissions to access it.
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        # use django authenticate to verify password and email match
        user = authenticate(request, email=email, password=password)
        # If our user is successfully authenticated...
        if user is not None:  
            login(request, user)
            # use django generate a token and save it to user
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)
            user.token = token.key
            user.save()
            # return the user with their id, email and token
            return Response({
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'token': token.key
                }
            })
        else:
            return Response({ 'msg': 'The username and/or password is incorrect.' }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class SignOut(generics.DestroyAPIView):
    def delete(self, request):
        user = request.user
        # Remove this token from the user
        Token.objects.filter(user=user).delete()
        user.token = None
        user.save()
        # Logout will remove all session data
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChangePasswordView(generics.CreateAPIView):
    serializer_class = ChangePasswordSerializer

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # if using drf authtoken, create a new token 
        if hasattr(user, 'auth_token'):
            user.auth_token.delete()
        token, created = Token.objects.get_or_create(user=user)
        # return new token
        return Response({'token': token.key}, status=status.HTTP_200_OK)
