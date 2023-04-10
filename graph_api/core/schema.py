import graphene
from core.models import Employee

from graph_api.core.type import EmployeeType
from django.core.exceptions import ObjectDoesNotExist
from graphql import GraphQLError


class EmployeeQuery(graphene.ObjectType):
    get_all_employees = graphene.List(
        EmployeeType, description="Returns List of all employees")
    get_employee = graphene.Field(
        EmployeeType, employee_id=graphene.ID(), description="Returns specific employee")

    def resolve_get_all_employees(root, info):
        return Employee.objects.all().order_by('-id')

    def resolve_get_employee(self, info, employee_id):
        try:
            employee_obj = Employee.objects.get(id=employee_id)
        except ObjectDoesNotExist:
            raise GraphQLError("Employee Does not exists!")
        return employee_obj
