from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('staff/', include('main.staff.urls')),
    path('position/', include('main.position.urls')),
    path('shift/', include('main.shift.urls')),
    path('staffshift/', include('main.staffshift.urls')),
    path('attandance/', include('main.attandance.urls')),
    path('fake-data/', views.create_fake_db_view, name='fake_data'),
]
