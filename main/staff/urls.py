from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.StaffHomeView.as_view(), name='staff-home'),
    path('create/', views.CreateStaffView.as_view(), name='staff-create'),
    path('update/<int:id>/', views.UpdateStaffView.as_view(), name='staff-update'),
    path('delete/<int:id>/', views.DeleteStaffView.as_view(), name='staff-delete'),
]