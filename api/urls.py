from django.urls import path
from api.views.auth_views import SignupView, VerifyEmail
from api.views.ops_views import FileUploadView
from api.views.client_views import FileListView, GenerateDownloadURL, EncryptedDownloadView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('client/signup/', SignupView.as_view()),
    path('client/verify-email/', VerifyEmail.as_view(), name='verify-email'),
    path('login/', TokenObtainPairView.as_view()),

    path('ops/upload/', FileUploadView.as_view()),

    path('client/files/', FileListView.as_view()),
    path('client/download/<int:file_id>/', GenerateDownloadURL.as_view()),
    path('client/download-link/<str:token>/', EncryptedDownloadView.as_view()),
]
