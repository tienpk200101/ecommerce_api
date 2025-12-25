import sys
import os
import django
from rest_framework.test import APIClient

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
django.setup()

from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

def test_auth():
    email = "hieuvt+1@mumesoft.vn"
    password = "tienpkph1324*"
    print(f"User Model: {User}")
    if User.objects.filter(email=email).exists():
        print("User already exists, deleting...")
        User.objects.get(email=email).delete()

    print("Creating user...")
    user = User.objects.create_user(email=email, password=password)
    print(f"User created: {user.email}")
    
    print("Calling API /api/v1/auth/login/...")
    client = APIClient()
    response = client.post('/api/v1/auth/login/', {
        'email': email,
        'password': password
    }, format='json')

    tokens = None

    print(f"Response Status Code: {response.status_code}")
    if response.status_code == 200:
        print("Login successful!")
        tokens = response.json()
    else:
        print(f"Login failed: {response.status_code}. Attempting to create user...")
        # Create user via UserViewSet? It requires IsAuthenticated probably.
        # But we need a user to test auth.
        # I'll create a superuser using manage.py if needed, but I cannot interact with it easily.
        # Let's assume I can create a user using the shell.

        print("Login FAILED!")
        print("Response:", response.json())
        return False

    print("Login Successful!")
    print("Tokens:", tokens)

if __name__ == "__main__":
    test_auth()
