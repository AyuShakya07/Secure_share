from rest_framework import serializers
from api.models import File

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['file']

    def validate_file(self, value):
        if not value.name.endswith(('.pptx', '.docx', '.xlsx')):
            raise serializers.ValidationError("Only pptx, docx, xlsx files allowed")
        return value

class FileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'file', 'uploaded_at']