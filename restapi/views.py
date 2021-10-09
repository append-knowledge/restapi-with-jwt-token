from django.shortcuts import render
from project.models import MyUser
from rest_framework.views import APIView
from rest_framework import mixins,generics
from restapi.serializer import Signupserializer,SignInserializer,UserDetailsserializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate,login,logout
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

# Create your views here.

class UserCreationView(generics.GenericAPIView,mixins.CreateModelMixin):
    serializer_class = Signupserializer
    model=MyUser


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserSignInviews(APIView):
    serializer_class= SignInserializer

    def post(self,request,*args,**kwargs):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            email=serializer.validated_data['email']
            password=serializer.validated_data['password']
            user=authenticate(request,username=email,password=password)
            if user:
                login(request,user)
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response({'msg':'login failed'},status=status.HTTP_400_BAD_REQUEST)


class Userlist(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin):
    serializer_class = UserDetailsserializer
    model=MyUser
    queryset = model.objects.all()
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)


class SelectedUser(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    serializer_class = UserDetailsserializer
    model=MyUser
    lookup_field = 'id'
    queryset = model.objects.all()
    # permission_classes = [IsAuthenticated]


    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)











