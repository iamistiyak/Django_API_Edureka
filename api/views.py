from django.shortcuts import render


from . serializers import EmployeeSerializer
from . models import Employees
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class EmployeeList(APIView):
       
    def get(self, request):
        employee_var = Employees.objects.all() 
        serializer = EmployeeSerializer(employee_var, many= True)
        return Response(serializer.data)    

        
class EmployeeData(APIView):
       
    def post(self, request):
        employee_var = Employees.objects.all() 
        serializer = EmployeeSerializer(employee_var, many= True)
        return Response(serializer.data)       