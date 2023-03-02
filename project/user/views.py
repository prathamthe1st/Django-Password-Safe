from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *
from .emails import *


# class to register a user and give response via api
# class RegisterAPI(APIView):
#     def post(self, request):
#         try:
#             data = request.data
#             serializer = UserSerializer(data = data)
#             if serializer.is_valid():
#                 serializer.save()
#                 send_otp(serializer.data['email'])
#                 return Response({
#                     'status' : 200,
#                     'message' : 'Email sent, check inbox!',
#                     'data' : serializer.data,
#                 })
#             return Response({
#                 'status' : 400,
#                 'message' : 'something went wrong',
#                 'data' : serializer.errors
#             })

#         except Exception as e:
#             print(e)


# function based view for user registration
@api_view(['POST'])
def Register(request):
    try:
            data = request.data
            serializer = UserSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                send_otp(serializer.data['email'])
                return Response({
                    'status' : 200,
                    'message' : 'Email sent, check inbox!',
                    'data' : serializer.data,
                })
            return Response({
                'status' : 400,
                'message' : 'something went wrong',
                'data' : serializer.errors
            })

    except Exception as e:
        print(e)

    return render(request, 'register.html')


# verifying otp from user
class VerifyOTP(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VerifyAccountSerializer(data = data)

            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']
                user = User.objects.filter(email = email)

                if not user.exists():
                    return Response({
                    'status' : 400,
                    'message' : 'something went wrong',
                    'data' : 'invalid email'
                })

                if not user[0].otp == otp:
                    return Response({
                    'status' : 400,
                    'message' : 'something went wrong',
                    'data' : 'OTP incorrect'
                })

                user = user.first()
                user.is_verified = True
                user.save()

                return Response({
                    'status' : 200,
                    'message' : 'Account Verified',
                    'data' : {}
                })

            return Response({
                'status' : 400,
                'message' : 'Something went wrong',
                'data' : serializer.errors
            })

        except Exception as e:
            print(e)