import requests
import json
import sys

BASE_URL = "http://localhost:8000"
USER_URL = f"{BASE_URL}/users/"
AUTH_URL = f"{BASE_URL}/api/auth/"

def test_auth_flow():
    print("Testing Auth Flow...")
    
    # 1. Create a user (if not exists)
    username = "testuser_jwt"
    password = "testpassword123"
    email = "testjwt@example.com"
    
    # Basic Auth to create user (admin/admin from fixtures or similar? Or just public registration?)
    # Wait, the UserViewSet might verify permissions.
    # Let's try to login first, if fail, try to create.
    
    # Try Login
    print(f"Attempting login for {username}...")
    login_data = {
        "username": username,
        "password": password
    }
    response = requests.post(f"{AUTH_URL}login/", data=login_data)
    
    tokens = None
    if response.status_code == 200:
        print("Login successful!")
        tokens = response.json()
    else:
        print(f"Login failed: {response.status_code}. Attempting to create user...")
        # Create user via UserViewSet? It requires IsAuthenticated probably.
        # But we need a user to test auth.
        # I'll create a superuser using manage.py if needed, but I cannot interact with it easily.
        # Let's assume I can create a user using the shell.
        return False

    print('Tokens', tokens)

    if tokens:
        print(f"Access Token: {tokens['data'].get('access')[:10]}...")
        print(f"Refresh Token: {tokens['data'].get('refresh')[:10]}...")
        
        # 2. Verify Token
        print("Verifying token...")
        verify_data = {"token": tokens['data']['access']}
        response = requests.post(f"{AUTH_URL}verify/", data=verify_data)
        if response.status_code == 200:
            print("Token valid.")
        else:
            print(f"Token verification failed: {response.status_code}")

        # 3. Refresh Token
        print("Refreshing token...")
        refresh_data = {"refresh": tokens['data']['refresh']}
        response = requests.post(f"{AUTH_URL}refresh/", data=refresh_data)
        if response.status_code == 200:
            print("Token refresh successful.")
            new_access = response.json().get('data').get('access')
            print(f"New Access Token: {new_access[:10]}...")
        else:
            print(f"Token refresh failed: {response.status_code}")
            
    return True

if __name__ == "__main__":
    success = test_auth_flow()
    if not success:
        print("Auth flow test could not complete fully (likely due to missing user).")
