from django.urls import path

urlpatterns = [
    path('team/', controllers.TeamList.as_view()),
    path('team/<int:pk>/', controllers.TeamDetail.as_view()),
    path('role/', controllers.RoleList.as_view()),
    path('role/<int:pk>/', controllers.RoleDetail.as_view()),
    path('event/', controllers.EventList.as_view()),
    path('event/<int:pk>/', controllers.EventDetail.as_view()),
    path('employee/', controllers.EmployeeList.as_view()),
    path('employee/<int:pk>/', controllers.EmployeeDetail.as_view()),
]
