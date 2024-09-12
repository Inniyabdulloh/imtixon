from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.StaffShiftHomeView.as_view(), name='staffshift-home'),
    path('update/<int:id>/', views.UpdateStaffShiftView.as_view(), name='staffshift-update'),
]