import random 
from datetime import timedelta
from django.utils import timezone
from .models import Staff, Position, Shift, StaffPosition, StaffShift, StaffAttandance

staff_data = [
    {'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'phone': 998901234567},
    {'first_name': 'Jane', 'last_name': 'Smith', 'age': 25, 'phone': 998901234568},
    {'first_name': 'Alice', 'last_name': 'Johnson', 'age': 28, 'phone': 998901234569},
    {'first_name': 'Bob', 'last_name': 'Williams', 'age': 35, 'phone': 998901234570},
    {'first_name': 'Charlie', 'last_name': 'Brown', 'age': 22, 'phone': 998901234571},
    {'first_name': 'David', 'last_name': 'JoTrue)', 'age': 40, 'phone': 998901234572},
    {'first_name': 'Eva', 'last_name': 'Davis', 'age': 27, 'phone': 998901234573},
    {'first_name': 'Frank', 'last_name': 'Garcia', 'age': 31, 'phone': 998901234574},
    {'first_name': 'Grace', 'last_name': 'Martinez', 'age': 29, 'phone': 998901234575},
    {'first_name': 'Hannah', 'last_name': 'Miller', 'age': 26, 'phone': 998901234576},
]


positions = [
    "Head Chef",
    "Chef",
    "Sous Chef",
    "Pastry Chef",
    "Line Cook",
    "Kitchen Assistant",
    "Restaurant Manager",
    "Front of House Manager",
    "Operations Manager",
    "Waiter",
]


shift_list = [
    {'start_time': '08:00', 'end_time':'13:00'},
    {'start_time': '13:00', 'end_time':'16:00'},
    {'start_time': '16:00', 'end_time':'21:00'},
]



def create_positions():
    for position in positions:
        Position.objects.create(name=position)


def create_staff():
    for staff in staff_data:
        Staff.objects.create(
            first_name=staff['first_name'],
            last_name=staff['last_name'],
            age=staff['age'],
            phone=staff['phone']
        )

def create_staff_position():
    staff_list = Staff.objects.filter(is_active=True)
    position_list = Position.objects.all()

    for staff, position in zip(staff_list, position_list):
        StaffPosition.objects.create(
            staff=staff,
            position=position
        )

def create_shift():
    for shift in shift_list:
        Shift.objects.create(
            start_time=shift['start_time'],
            end_time=shift['end_time']
        )


def create_staff_shift():
    staff_list = Staff.objects.filter(is_active=True)
    shift_list = Shift.objects.all()

    random_shift = random.choice(shift_list)

    for staff in staff_list:
        StaffShift.objects.create(
            staff=staff,
            shift=random_shift
        )


def create_staff_attendance():
    # Barcha xodimlarni olish
    staff_list = Staff.objects.filter(is_active=True)

    for _ in range(5):

        for staff in staff_list:
            # Tasodifiy vaqt oralig'ida check_in va check_out generatsiya qilish
            check_in_time = timezone.now() - timedelta(days=random.randint(0, 30), hours=random.randint(0, 8))
            check_out_time = check_in_time + timedelta(hours=random.randint(1, 8))  # 1 dan 8 soatgacha ishlagan vaqt

            # Attendance ma'lumotlarini saqlash
            StaffAttandance.objects.create(
                staff=staff,
                check_in=check_in_time,
                check_out=check_out_time
            )


if __name__ == 'main':
    create_positions()
    create_staff()
    create_staff_position()
    create_shift()
    create_staff_shift()
    create_staff_attendance()