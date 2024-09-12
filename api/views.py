from rest_framework import generics
from main import models
from . import serializers

class StaffListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Staff.objects.all()
    serializer_class = serializers.StaffSerializer


class StaffRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Staff.objects.all()
    serializer_class = serializers.StaffSerializer


class StaffPositionListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.StaffPosition.objects.all()
    serializer_class = serializers.StaffPositionSerializer


class StaffPositionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.StaffPosition.objects.all()
    serializer_class = serializers.StaffPositionSerializer


class ShiftListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Shift.objects.all()
    serializer_class = serializers.ShiftSerializer


class ShiftRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Shift.objects.all()
    serializer_class = serializers.ShiftSerializer


class StaffShiftListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.StaffShift.objects.all()
    serializer_class = serializers.StaffShiftSerializer


class StaffShiftRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.StaffShift.objects.all()
    serializer_class = serializers.StaffShiftSerializer



class StaffAttandanceListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.StaffAttandance.objects.all()
    serializer_class = serializers.StaffAttandanceSerializer


class StaffAttandanceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.StaffAttandance.objects.all()
    serializer_class = serializers.StaffAttandanceSerializer    


class PositionListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Position.objects.all()
    serializer_class = serializers.PositionSerializer


class PositionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Position.objects.all()
    serializer_class = serializers.PositionSerializer