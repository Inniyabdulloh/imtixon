from django.contrib.auth.mixins import UserPassesTestMixin
from main import models
from django.shortcuts import render, redirect
from django.views import View



class StaffHomeView(UserPassesTestMixin, View):

    def get(self, request):
        staff_list = models.Staff.objects.filter(is_active=True)
        return render(request, 'staff/home.html', {'staff_list': staff_list})
    
    def test_func(self):
        return self.request.user.is_staff


class CreateStaffView(UserPassesTestMixin, View):
    def get(self, request):
        position_list = models.Position.objects.all()
        shift_list = models.Shift.objects.all()
        return render(request,'staff/create.html', {'position_list':position_list, 'shift_list': shift_list})

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = int(request.POST.get('age'))
        phone_number = int(request.POST.get('phone'))
        position = models.Position.objects.get(id=int(request.POST.get('position')))

        staff = models.Staff.objects.create(
            first_name=first_name,
            last_name=last_name,
            age=age,
            phone=phone_number,
        )
        models.StaffPosition.objects.create(
            staff=staff,
            position=position
        )

        return redirect('staff-home')

    def test_func(self):
        return self.request.user.is_staff


class UpdateStaffView(UserPassesTestMixin, View):
    def get(self, request, id):
        staff = models.Staff.objects.get(id=id)
        position_list = models.Position.objects.all()
        return render(request, 'staff/update.html', {'staff': staff, 'position_list': position_list})
    
    def post(self, request, id):
        staff = models.Staff.objects.get(id=id)
        position = models.Position.objects.get(id=int(request.POST.get('position')))
        shift = models.Shift.objects.get(id=int(request.POST.get('shift')))
        staff.first_name = request.POST.get('first_name')
        staff.last_name = request.POST.get('last_name')
        staff.age = int(request.POST.get('age'))
        staff.phone = int(request.POST.get('phone'))
        staff.save()
        stf = models.StaffPosition.objects.get(staff=staff)
        stfaf_shift = models.StaffShift.objects.create(
            staff=staff,
            shift=shift
        )
        stfaf_shift.save()
        stf.position = position
        stf.save()
        staff.refresh_from_db()

        return redirect('staff-update', id=id)

    def test_func(self):
        return self.request.user.is_staff


class DeleteStaffView(UserPassesTestMixin, View):
    def get(self, request, id):
        staff = models.Staff.objects.get(id=id)
        staff.is_active = False
        staff.save()
        return redirect('staff-home')

    def test_func(self):
        return self.request.user.is_staff