from rest_framework import serializers
from .models import Employees

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        # fields = ['emp_id', 'firest_name', 'last_name', ]
        fields= '__all__'   
        