from main import models
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import View

class PositionHomeView(UserPassesTestMixin, View):

    def get(self, request):
        postion_list = models.Position.objects.all()
        return render(request, 'position/home.html', {'position_list':postion_list})
    
    def test_func(self):
        return self.request.user.is_staff


class CreatePositionView(UserPassesTestMixin, View):
    def get(self, request):
        return render(request, 'position/create.html')
    
    def post(self, request):
        models.Position.objects.create(
            name=request.POST.get('name')
        )
        return redirect('position-home')
    
    def test_func(self):
        return self.request.user.is_staff
    

class UpdatePositionView(UserPassesTestMixin, View):
    def get(self, request, id):
        position = models.Position.objects.get(id=id)
        return render(request, 'position/update.html', {'position': position})  


    def post(self, request, id):
        position = models.Position.objects.get(id=id)
        position.name = request.POST.get('name')
        position.save()

        return redirect('position-home')
    
    def test_func(self):
        return self.request.user.is_staff
    

class DeletePositionView(UserPassesTestMixin, View):
    def get(self, request, id):
        models.Position.objects.get(id=id).delete() 

        return redirect('position-home')
    
    def test_func(self):
        return self.request.user.is_staff