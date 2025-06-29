from dj_rest_auth.registration.serializers import SocialLoginSerializer

class GoogleLoginSerializer(SocialLoginSerializer):
    def validate(self, attrs):
        # Use id_token as access_token if needed
        if not attrs.get('access_token') and 'id_token' in self.context['request'].data:
            attrs['access_token'] = self.context['request'].data['id_token']
        return super().validate(attrs)