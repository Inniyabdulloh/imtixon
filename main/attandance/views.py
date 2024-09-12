from main import models
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import View

class AttandanceHomeView(UserPassesTestMixin, View):

    def get(self, request):
        attandance_list = models.StaffAttandance.objects.filter(staff__is_active=True)
        return render(request, 'attandance/home.html', {'attandance_list':attandance_list})
    
    def test_func(self):
        return self.request.user.is_staff