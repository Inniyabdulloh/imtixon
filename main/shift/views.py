from main import models
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import View

class ShiftHomeView(UserPassesTestMixin, View):

    def get(self, request):
        shift_list = models.Shift.objects.all()
        return render(request, 'shift/home.html', {'shift_list':shift_list})
    
    def test_func(self):
        return self.request.user.is_staff


class CreateShiftView(UserPassesTestMixin, View):
    def get(self, request):
        return render(request, 'shift/create.html')
    
    def post(self, request):
        models.Shift.objects.create(
            start_time=request.POST.get('start-time'),
            end_time=request.POST.get('end-time')
        )
        return redirect('shift-home')
    
    def test_func(self):
        return self.request.user.is_staff
    

class UpdateShiftView(UserPassesTestMixin, View):
    def get(self, request, id):
        shift = models.Shift.objects.get(id=id)
        return render(request, 'shift/update.html', {'shift': shift})  


    def post(self, request, id):
        shift = models.Shift.objects.get(id=id) 
        shift.start_time = request.POST.get('start-time')
        shift.end_time = request.POST.get('end-time')
        shift.save()

        return redirect('shift-home')
    
    def test_func(self):
        return self.request.user.is_staff
    

class DeleteShiftView(UserPassesTestMixin, View):
    def get(self, request, id):
        models.Shift.objects.get(id=id).delete() 

        return redirect('shift-home')
    
    def test_func(self):
        return self.request.user.is_staff