from django.urls import path
from api import controllers
from rest_framework import routers
from django.views.decorators.csrf import csrf_exempt

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    #path('user', controllers.UserList.as_view()),
    #path('user/<int:pk>', controllers.UserDetail.as_view()),
    path('register', csrf_exempt(controllers.Register.as_view())),
    path('session', csrf_exempt(controllers.Session.as_view())),
    path('team', controllers.TeamList.as_view()),
    path('team/<int:pk>', controllers.TeamDetail.as_view()),
    path('role', controllers.RoleList.as_view()),
    path('role/<int:pk>', controllers.RoleDetail.as_view()),
    path('event', controllers.EventList.as_view()),
    path('event/<int:pk>', controllers.EventDetail.as_view()),
    path('employee', controllers.EmployeeList.as_view()),
    path('employee/<int:pk>', controllers.EmployeeDetail.as_view()),
]
