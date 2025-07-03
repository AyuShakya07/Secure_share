from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.urls import reverse
from api.serializers.user_serializers import SignupSerializer
from api.models import User
from api.utils import generate_encrypted_token, decode_encrypted_token

class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = generate_encrypted_token(user.id)
            verify_url = request.build_absolute_uri(reverse('verify-email')) + f'?token={token}'
            send_mail('Verify Email', f'Click to verify: {verify_url}', 'admin@site.com', [user.email])
            return Response({"message": "Signup successful. Check email to verify."}, status=201)
        return Response(serializer.errors, status=400)

class VerifyEmail(APIView):
    def get(self, request):
        try:
            data = decode_encrypted_token(request.GET.get('token'))
            user = User.objects.get(id=data['file_id'])
            user.is_active = True
            user.is_verified = True
            user.save()
            return Response({"message": "Email verified successfully"})
        except Exception:
            return Response({"error": "Invalid or expired token"}, status=400)
