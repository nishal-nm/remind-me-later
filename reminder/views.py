from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReminderSerializer


# Create your views here.
@api_view(["POST"])
def create_reminder(request):
    serializer = ReminderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "message stored successfully", "data": serializer.data},
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
