from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from .serializers import GoogleLoginSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import User
from .serializers import UserDetailsSerializer

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    serializer_class = GoogleLoginSerializer
    
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_staff']