from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializer import *
from .email import *
from rest_framework import views


class Send_otp(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data = data)
            usr = client.objects.filter(email = data['email'])
            if usr:
                send_otp(request.data['email'])
                return Response({'status':200,'message':'OTP Send Successfull','data':request.data['email']})
            if serializer.is_valid():
                serializer.save()
                send_otp(serializer.data['email'])
                return Response({'status':200,'message':'OTP created succesfull check email','data':serializer.data })
            return Response({'status':400,'message':'Something went Wrong','data':serializer.errors})
        except Exception as e:
            print(e)

class verify_otp(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = verifyaccount(data = data)
            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']
                user = client.objects.filter(email = email)
                if not user.exists():
                    return Response({
                    'status':400,
                    'message':'Something went Wrong',
                    'data':'invalid email'
                    })
                if user[0].otp != otp:
                    return Response({
                    'status':400,
                    'message':'Something went Wrong',
                    'data':'wrong otp'
                    })
                user.update(is_verified = True)
                return Response({
                    'status':200,
                    'message':'account verified',
                    'data':{}
                })
            return Response({
                'status':400,
                'message':'Something went Wrong',
                'data':serializer.errors
            })
        except Exception as e:
            print(e)