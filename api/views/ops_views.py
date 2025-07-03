from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from api.serializers.file_serializers import FileUploadSerializer
from api.permissions import IsOpsUser
from rest_framework.response import Response

class FileUploadView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsOpsUser]

    def post(self, request):
        print("FILES:", request.FILES)
        print("DATA:", request.data)

        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(uploaded_by=request.user)
            return Response({"message": "File uploaded"}, status=201)
        print("Errors:", serializer.errors)
        return Response(serializer.errors, status=400)

