from django.contrib.auth.models import  User
from django.contrib.auth import authenticate

from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from .serializers import  UserSerializer,SignupSerializer,LoginSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]



class UserProfile(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        serializer=UserSerializer(request.user)
        return Response(serializer.data)
    

class UserRegister(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self,request):
        print(request.data)
        serializer=SignupSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data["username"]
            email = serializer.data["email"]
            password = serializer.data["password"]
            user = User.objects.create(username=username,email=email)
            user.set_password(password)
            user.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    

class UserLogin(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self,request):
        user = request.user
        serializer=LoginSerializer(data = request.data)
        if serializer.is_valid():
            username = serializer.data["username"]
            password = serializer.data["password"]
            user = authenticate(username=username,password=password)
            print(user)
            if user :
                token, created= Token.objects.get_or_create(user=user)
                return Response({"token":token.key} ,status=200)
        else:
            return Response({"errors":"invalid credition"})

