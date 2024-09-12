from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Staff(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    phone = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def position(self):
        return StaffPosition.objects.get(staff=self).position.name
    
    @property
    def shift(self):
        return StaffShift.objects.get(staff=self).shift

class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    

class StaffPosition(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.staff} - {self.position}"

    @property
    def staff_list(self):
        return 0

class Shift(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self) -> str:
        return f"{self.start_time} - {self.end_time}"

        
class StaffShift(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.staff} {self.shift}"
    


class StaffAttandance(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    check_in = models.DateTimeField(auto_now_add=True)
    check_out = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.staff} - {self.check_in} - {self.check_out}"


