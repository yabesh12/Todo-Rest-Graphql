import graphene
from graphql import GraphQLError
from core.models import Employee
from graph_api.core.type import EmployeeType

from graph_api.core.utils import validate_mobile_number
from django.core.exceptions import ObjectDoesNotExist


class CreateEmployee(graphene.Mutation):
    """
    :params:name, designation, mobile, location(optional)
    :returns: Success response with employee details If valid data
    """
    class Arguments:
        name = graphene.String(required=True)
        designation = graphene.String(required=True)
        mobile_number = graphene.String(required=True)
        location = graphene.String()

    status = graphene.String()
    message = graphene.String()
    employee_details = graphene.Field(EmployeeType)

    def mutate(self, info, name, designation, mobile_number, *args, **kwargs):
        validated_mobile_no = validate_mobile_number(mobile_number)
        if len(name) <= 2 or name.isdigit():
            raise GraphQLError("Name should be valid!")
        if len(designation) <= 2 or designation.isdigit():
            raise GraphQLError("Designation should be valid!")
        if location := kwargs.get("location") is not None:
            if len(location) <= 3 and not name.isdigit():
                raise GraphQLError("Location should be valid!")
        employee_obj = Employee.objects.create(name=name, mobile_number=validated_mobile_no,
                                               designation=designation, location=location)

        return CreateEmployee(status="Success", message="Employee Details Created Successfully!",
                              employee_details=employee_obj)


class UpdateEmployee(graphene.Mutation):
    """
    :params:id, name(optional), designation(optional), mobile(optional), location(optional)
    :returns: Success response with updated employee details If valid data
    """
    class Arguments:
        employee_id = graphene.ID(required=True)
        name = graphene.String()
        designation = graphene.String()
        mobile_number = graphene.String()
        location = graphene.String()

    status = graphene.String()
    message = graphene.String()
    employee_details = graphene.Field(EmployeeType)

    def mutate(self, info, employee_id, *args, **kwargs):
        try:
            employee_obj = Employee.objects.get(id=employee_id)
        except ObjectDoesNotExist:
            raise GraphQLError("Employee Does Not Exists!")

        if employee_obj is not None:
            if name_new := kwargs.get('name'):
                print("H")
                print(name_new)
                if len(name_new) <= 2 or name_new.isdigit():
                    raise GraphQLError("Name should be valid!")
                employee_obj.name = name_new
            if designation_new := kwargs.get('designation'):
                if len(designation_new) <= 2 or designation_new.isdigit():
                    raise GraphQLError("Designation should be valid!")
                employee_obj.designation = designation_new
            if mobile_new := kwargs.get('mobile_number'):
                validate_mobile_number(mobile_new)
                employee_obj.mobile_number = mobile_new
            if location_new := kwargs.get('location'):
                if len(location_new) <= 2 or location_new.isdigit():
                    raise GraphQLError("Location should be valid!")
                employee_obj.location = location_new
            employee_obj.save()
        return UpdateEmployee(status="Success", message="Employee details updated Successfully!", employee_details=employee_obj)


class DeleteEmployee(graphene.Mutation):
    """
    :params:Employee id(required)
    :returns:employee details deleted if employee exists
    """
    class Arguments:
        employee_id = graphene.ID(required=True)

    status = graphene.String()
    message = graphene.String()

    def mutate(self, info, employee_id):
        try:
            employee_obj = Employee.objects.get(id=employee_id)
        except ObjectDoesNotExist:
            raise GraphQLError("Employee Does Not Exists!")

        if employee_obj is not None:
            employee_obj.delete()

        return DeleteEmployee(status="Success", message="Employee details deleted Successfully!")


class EmployeeMutations(graphene.ObjectType):
    create_employee = CreateEmployee.Field()
    update_employee = UpdateEmployee.Field()
    delete_employee = DeleteEmployee.Field()
