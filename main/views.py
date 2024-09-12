from django.shortcuts import render
from . import fake_data
# Create your views here.
def create_fake_db_view(request):
    fake_data.create_staff()
    fake_data.create_positions()
    fake_data.create_staff_position()
    fake_data.create_shift()
    fake_data.create_staff_shift()
    fake_data.create_staff_attendance()

    return render(request, 'create_fake_db.html')

def home_page(request):
    return render(request, 'index.html')



