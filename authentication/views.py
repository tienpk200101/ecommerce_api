from django.http.response import JsonResponse
from rest_framework import viewsets, filters
from authentication.models import Person, Group, Membership
from django.db.models import Value
from django.db.models.functions import Concat
from authentication.serializers import PersonSerializer, GroupSerializer, MembershipSerializer
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'email']


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['person__first_name', 'person__last_name', 'group__name']


class PersonListView:
    queryset = Person.objects.all()


def hello_view(request):
    persons = Person.objects.all()
    return render(request, "hello_world.html", {'persons': persons})