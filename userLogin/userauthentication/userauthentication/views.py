from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import UserLoginSerializer, UserRegisterSerializer, EmpolyeeSerializers
from db.models import Empolyee

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserLoginViews(APIView):

    def post(self,request):
        data =request.data
        seri = UserLoginSerializer(data = data)
        if seri.is_valid():
            user = authenticate(username = data["username"],password = data["password"])
            if user:

                return Response({
                    "Data" : seri.data,
                "Message" : "User authenticate sucessfully"
                })

            return Response({
                "Data" : seri.data,
                "Message" : "User credentials are wrong"
            })
        return Response(seri.errors)

class UserRegisterView(APIView):

    def get(self,request):
        obj = User.objects.all()
        seri = UserRegisterSerializer(obj, many= True)
        return Response(seri.data)
    
    def post(self,request):
        data = request.data
        seri = UserRegisterSerializer(data=data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data)
        
        return Response(seri.errors)
    
class EmpolyeeView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        obj = Empolyee.objects.all()
        print(obj)
        seri = EmpolyeeSerializers(obj, many=True)
        return Response(seri.data)