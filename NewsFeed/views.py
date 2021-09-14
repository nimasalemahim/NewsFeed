from .signupSerializer import SignUpSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class SignupView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        return Response(data={'Token': user.token})
