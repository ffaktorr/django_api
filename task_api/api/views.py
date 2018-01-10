from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employees, Departments
from .serializers import EmployeesSerializer, DepartmentsSerializer


class EmployeesList(APIView):

    def get(self, *args, **kwargs):
        if "token" in self.request.query_params.keys():
            if self.request.query_params['token'] == "123":
                employees = Employees.objects.all()
                serializer = EmployeesSerializer(employees, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid token!'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'token missing!'}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, *args, **kwargs):

        if "token" in self.request.query_params.keys():
            if self.request.query_params['token'] == "123":
                if 'first_name' in self.request.data.keys():
                    first_name = self.request.data['first_name']
                else:
                    first_name = self.request.query_params.get('first_name', None)

                if 'last_name' in self.request.data.keys():
                    last_name = self.request.data['last_name']
                else:
                    last_name = self.request.query_params.get('last_name', None)

                if 'department' in self.request.data.keys():
                    department = self.request.data['department']
                else:
                    department = self.request.query_params.get('department', None)
                data = {
                    "first_name": first_name,
                    "last_name": last_name,
                    "department": department,
                }
                serializer = EmployeesSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Invalid token!'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'token missing!'}, status=status.HTTP_401_UNAUTHORIZED)


class DepartmentsList(APIView):

    def get(self, *args, **kwargs):
        if "token" in self.request.query_params.keys():
            if self.request.query_params['token'] == "123":
                departments = Departments.objects.all()
                serializer = DepartmentsSerializer(departments, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid token!'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'token missing!'}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, *args, **kwargs):

        if "token" in self.request.query_params.keys():
            if self.request.query_params['token'] == "123":
                if "name" in self.request.data.keys():
                    name = self.request.data['name']
                else:
                    name = self.request.query_params.get('name', None)
                data = {
                    "name": name
                }
                serializer = DepartmentsSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Invalid token!'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'token missing!'}, status=status.HTTP_401_UNAUTHORIZED)


class DefaultAPIView(APIView):

    def get(self, *args, **kwargs):
        return Response("{'error': 'Access Forbidden!'}", status=status.HTTP_403_FORBIDDEN)

    def post(self, *args, **kwargs):
        return Response("{'error': 'Access Forbidden!'}", status=status.HTTP_403_FORBIDDEN)
