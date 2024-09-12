from rest_framework import serializers
from main.models import Staff, Position, StaffPosition, Shift, StaffShift, StaffAttandance

class StaffSerializer(serializers.ModelSerializer):
    position = serializers.CharField(source='position', read_only=True)
    shift = serializers.CharField(source='shift', read_only=True)

    class Meta:
        model = Staff
        fields = ['id', 'first_name', 'last_name', 'age', 'phone', 'is_active', 'position', 'shift']


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'name']


class StaffPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffPosition
        fields = ['id', 'staff', 'position']


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = ['id', 'start_time', 'end_time']


class StaffShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffShift
        fields = ['id', 'staff', 'shift']


class StaffAttandanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffAttandance
        fields = ['id', 'staff', 'check_in', 'check_out']
