from main import models
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import View

class StaffShiftHomeView(UserPassesTestMixin, View):

    def get(self, request):
        staffshift_list = models.StaffShift.objects.all()
        return render(request, 'staffshift/home.html', {'staffshift_list':staffshift_list})
    
    def test_func(self):
        return self.request.user.is_staff



    

class UpdateStaffShiftView(UserPassesTestMixin, View):
    def get(self, request, id):
        staffshift = models.StaffShift.objects.get(id=id)
        shift_list = models.Shift.objects.all()
        return render(request, 'staffshift/update.html', {'staffshift': staffshift, 'shift_list':shift_list})  


    def post(self, request, id):
        staffshift = models.StaffShift.objects.get(id=id) 
        shift = models.Shift.objects.get(id=int(request.POST.get('shift')))
        staffshift.shift = shift
        staffshift.save()

        return redirect('staffshift-home')
    
    def test_func(self):
        return self.request.user.is_staff