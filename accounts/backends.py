from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Check if the input username is an email address
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            # If the input username is not an email, try to authenticate using the username
            user = User.objects.get(username=username)
        if user.check_password(password):
            return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
