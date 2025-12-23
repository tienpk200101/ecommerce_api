from django.db import models

# Create your models here.
class Account(models.Model):
    id = models.UUIDField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'account'