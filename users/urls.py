from . import views

from rest_framework import routers
from django.urls import path , include




router_user = routers.DefaultRouter()

router_user.register('user', views.UserList)



router_users = routers.DefaultRouter()


router_users.register('users', views.UsersList)


router_job = routers.DefaultRouter()


router_job.register('job', views.JobList)


urlpatterns = [
path('', include(router_user.urls)) ,
path('', include(router_users.urls)) ,
path('', include(router_job.urls)) ,
]

