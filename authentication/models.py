import uuid

from django.db import models


# Create your models here.
class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    birth_date = models.DateField(null=True)

    class Meta:
        db_table = 'authentication_person'

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


class Group(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    members = models.ManyToManyField(Person, through='Membership', related_name='groups')

    def __str__(self):
        return self.name


class Membership(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField(null=True)

    def __str__(self):
        return f"{self.person} - {self.group}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['person', 'group'], name='unique_person_group'
            )
        ]
