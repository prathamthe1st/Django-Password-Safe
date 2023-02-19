from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *


# function to register a user and give response via api
class RegisterAPI(APIView):

    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
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
            