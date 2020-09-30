
from employees.models import Employee
from employees.api.serializers import EmployeeSerializer
from rest_framework import viewsets

class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer