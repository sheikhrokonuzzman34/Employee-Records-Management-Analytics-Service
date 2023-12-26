from django.shortcuts import render

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count, Avg
from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer

class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeAnalyticsView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'employee_count_by_department': Employee.objects.values('department__name').annotate(count=Count('id')),
            'average_tenure': Employee.objects.aggregate(avg_tenure=Avg('tenure')),
            # Add more analytics as needed
        }
        return Response(data)





def home(request):
    return render(request, 'mainapp/home.html')
