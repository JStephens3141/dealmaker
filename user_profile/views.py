import random
from user_profile.models import Profile
from rest_framework import response, status
from rest_framework.views import APIView

# TODO: Limit resutls to is_broker attribute

class ProfileAPIView(APIView):
    def get(self, _):
        profiles = Profile.objects.all()
        profile = random.choice(profiles)
        return response({
            'id': profile.id
        },
            status=status.HTTP_200_OK
        )

