import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from django.contrib.auth.models import User

def create_user():
    username = "testuser_jwt"
    password = "testpassword123"
    email = "testjwt@example.com"
    
    if User.objects.filter(username=username).exists():
        print(f"User {username} already exists.")
        return

    User.objects.create_user(username=username, password=password, email=email)
    print(f"User {username} created successfully.")

if __name__ == "__main__":
    create_user()
