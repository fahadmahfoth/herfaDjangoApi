from django.shortcuts import render
from rest_framework.permissions import IsAdminUser ,BasePermission,SAFE_METHODS
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import JobsSerializer , UsersSerializer , UserSerializer 
from .models import Jobs , Users 
from django_filters.rest_framework import DjangoFilterBackend



# Create your views here.

class ReadOnly(BasePermission):

    def has_permission(self, request, view):
        
        return request.method in SAFE_METHODS



class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UsersList(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'job',]



class JobList(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']
    permission_classes = [IsAdminUser|ReadOnly]
