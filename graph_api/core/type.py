from graphene_django import DjangoObjectType

from core.models import Employee


class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee
        fields = "__all__"