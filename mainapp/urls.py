from django.urls import path
from .views import *


urlpatterns = [
    path('departments/', DepartmentListCreateView.as_view(), name='department-list-create'),
    path('departments/<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('analytics/', EmployeeAnalyticsView.as_view(), name='employee-analytics'),
    
    
    
    path('',home,name='home'),
]
