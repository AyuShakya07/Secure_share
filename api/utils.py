from itsdangerous import URLSafeSerializer
from django.conf import settings

serializer = URLSafeSerializer("super-secret-key", salt="download")

def generate_encrypted_token(file_id):
    return serializer.dumps({'file_id': file_id})

def decode_encrypted_token(token):
    return serializer.loads(token)