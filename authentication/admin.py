from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Customize UserAdmin if needed, or just register it
admin.site.register(User)
