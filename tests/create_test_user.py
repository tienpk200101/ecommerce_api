import os
import sys
import django

# Add the project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from django.contrib.auth import get_user_model

def create_user():
    User = get_user_model()
    email = "tienpk+1@mumesoft.vn"
    password = "tienpkph13248"
    
    # User.objects is the instance of UserManager
    # You can call your custom method if you defined it, or basic filter
    # Note: custom methods on Manager are called via User.objects
    
    if User.objects.check_user_exist(email):
        print(f"User {email} already exists.")
        return

    User.objects.create_superuser(email=email, password=password)
    print(f"User {email} created successfully.")

if __name__ == "__main__":
    create_user()
