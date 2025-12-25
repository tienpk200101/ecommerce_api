import sys
import os
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
django.setup()

from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()
email = "newuser@example.com"
password = "StrongPassword@123"

# Ensure user doesn't exist
if User.objects.filter(email=email).exists():
    User.objects.get(email=email).delete()

client = APIClient()
data = {
    'email': email,
    'password': password,
    'password_confirm': password
}

print("Calling API /api/v1/auth/register/...")
response = client.post('/api/v1/auth/register/', data, format='json')

print(f"Status: {response.status_code}")
if response.status_code == 201:
    tokens = response.json()
    print("Registration Successful!", tokens['data'])
    if 'access' in tokens['data'] and 'refresh' in tokens['data']:
        print("Tokens found in response!")
        print(f"Access Token: {tokens['data']['access'][:20]}...")
    else:
        print("ERROR: Tokens MISSING in response!")
        print(tokens)
else:
    print("Registration FAILED!")
    print(response.json())
