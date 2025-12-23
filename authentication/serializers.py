from rest_framework import serializers
from authentication.models import Person, Group, Membership


# class PersonListSerializer(serializers.ModelSerializer):
#     def to_representation(self, instance):
#         if not instance.exists():
#             return {
#                 "error_message": "Not Found!"
#             }

#         return {
#             "data": super().to_representation(instance),
#             "message": "success",
#             "status": 200,
#         }

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
        # list_serializer_class = PersonListSerializer


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = "__all__"