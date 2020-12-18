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
    path('teams', controllers.TeamList.as_view()),
    path('teams/<int:pk>', controllers.TeamDetail.as_view()),
    path('shiftevents', controllers.ShifteventList.as_view()),
    path('shiftevents/<int:pk>', controllers.ShifteventDetail.as_view()),
    path('oooevents', controllers.OooeventList.as_view()),
    path('oooevents/<int:pk>', controllers.OooeventDetail.as_view()),
    path('employees', controllers.EmployeeList.as_view()),
    path('employees/<int:pk>', controllers.EmployeeDetail.as_view()),
]
