import json

from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import status

from .producer_user_created import ProducerUserCreated
from .serializer import RegisterSerializer


# Create your views here.
class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    producer = ProducerUserCreated()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.data)

        if serializer.is_valid(raise_exception = True):
            self.perform_create(serializer=serializer)
            self.producer.publish("user_created_method", body=serializer.data)
            headers = self.get_success_headers(data=serializer.data)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(data=serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY )

            