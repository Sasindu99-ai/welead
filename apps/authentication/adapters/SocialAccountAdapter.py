from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import login
from django.shortcuts import redirect

from apps.authentication.models import User

__all__ = ["SocialAccountAdapter"]


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        user_email = sociallogin.account.extra_data.get("email")
        if user_email:
            try:
                user = User.objects.filter(email=user_email).first()
                if user is None:
                    user = User(email=user_email)
                    user.save()
                sociallogin.connect(request, user)
                login(request, user)
                return redirect("/")
            except User.DoesNotExist:
                pass  # Let Allauth handle the new signup normally
