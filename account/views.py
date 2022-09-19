from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class UserRegistrationView(APIView):
    def post(self, request, format = None):
        serializer = UserRegistrationSerializer(data = request.data)
        return Response({'msg': 'Registration Success'})

