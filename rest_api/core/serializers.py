from rest_framework import serializers
from core.models import Employee
from graph_api.core.utils import validate_mobile_number

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
    
    def validate_name(self, name):
        if len(name) <=2 or name.isdigit():
            raise serializers.ValidationError("Name should be Valid!")
        return name
    
    def validate_mobile_number(self, mobile_number):
        """
        Validates the mobile number.
        """
        # if not mobile_number.isdigit()
        if not mobile_number.isdigit():
            raise serializers.ValidationError("Please enter a valid phone number")
        if len(mobile_number) != 10:
            raise serializers.ValidationError("Please enter a valid phone number")
        else:
            return mobile_number
    
    def validate_designation(self, designation):
        if len(designation) <=2 or designation.isdigit():
            raise serializers.ValidationError("Designation should be Valid!")
        return designation
    
    def validate_location(self, *args, **kwargs):
        if kwargs.get("location") is not None:
            location = kwargs.get("location")
            if len(location) <=2 or location.isdigit():
                raise serializers.ValidationError("Location should be Valid!")
            return location