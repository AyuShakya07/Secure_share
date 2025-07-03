from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import FileResponse
from api.models import File
from api.serializers.file_serializers import FileListSerializer
from api.permissions import IsClientUser
from api.utils import generate_encrypted_token, decode_encrypted_token

class FileListView(APIView):
    permission_classes = [IsClientUser]

    def get(self, request):
        files = File.objects.all()
        return Response(FileListSerializer(files, many=True).data)

class GenerateDownloadURL(APIView):
    permission_classes = [IsClientUser]

    def get(self, request, file_id):
        try:
            File.objects.get(id=file_id)
            token = generate_encrypted_token(file_id)
            url = request.build_absolute_uri(f"/api/client/download-link/{token}/")
            return Response({"download-link": url, "message": "success"})
        except File.DoesNotExist:
            return Response({"error": "File not found"}, status=404)

class EncryptedDownloadView(APIView):
    permission_classes = [IsClientUser]

    def get(self, request, token):
        try:
            data = decode_encrypted_token(token)
            file = File.objects.get(id=data['file_id'])
            return FileResponse(file.file, as_attachment=True)
        except Exception:
            return Response({"error": "Invalid token or file"}, status=400)