""" Handler for auth tokens. """
from rest_framework.authtoken.models import Token


def get_auth_token(user):
    """
    Get or create token for user object
    Args:
         user(object): user instance
    Returns:
        token(str): User valid token
    """
    token, status = Token.objects.get_or_create(user=user)
    return token.key
