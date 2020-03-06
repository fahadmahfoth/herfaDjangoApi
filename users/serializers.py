from rest_framework import  serializers
from django.contrib.auth.models import User
from . models import Jobs , Users






class UsersSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    jobName = serializers.CharField(source='job.job', read_only=True)
    
    class Meta:
        model = Users
        fields = ['id','user','username','fullName','phoneNumber','jobName','area','job','whatsApp','date']




class JobsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jobs
        fields = ['id','job']



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name','is_staff','is_superuser']


