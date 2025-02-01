from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import StandardSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class StandardAPIView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        serialized = StandardSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response({'data': serialized.data})
        else:
            return Response({'errors': serialized.errors}, status=status.HTTP_400_BAD_REQUEST)

