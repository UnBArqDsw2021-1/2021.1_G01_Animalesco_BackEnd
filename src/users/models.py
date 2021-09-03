from django.contrib.auth import get_user_model
from django.contrib.auth.models import User as DjangoUser

User = get_user_model()
