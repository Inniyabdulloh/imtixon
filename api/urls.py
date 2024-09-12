from django.urls import path
from . import views

urlpatterns = [
    path('staff/', views.StaffListCreateAPIView.as_view(), name='staff-list-create'),
    path('staff/<int:pk>/', views.StaffRetrieveUpdateDestroyAPIView.as_view(), name='staff-detail'),
    
    path('position/', views.PositionListCreateAPIView.as_view(), name='position-list-create'),
    path('position/<int:pk>/', views.PositionRetrieveUpdateDestroyAPIView.as_view(), name='position-detail'),
    
    path('staff-position/', views.StaffPositionListCreateAPIView.as_view(), name='staff-position-list-create'),
    path('staff-position/<int:pk>/', views.StaffPositionRetrieveUpdateDestroyAPIView.as_view(), name='staff-position-detail'),
    
    path('shift/', views.ShiftListCreateAPIView.as_view(), name='shift-list-create'),
    path('shift/<int:pk>/', views.ShiftRetrieveUpdateDestroyAPIView.as_view(), name='shift-detail'),
    
    path('staff-shift/', views.StaffShiftListCreateAPIView.as_view(), name='staff-shift-list-create'),
    path('staff-shift/<int:pk>/', views.StaffShiftRetrieveUpdateDestroyAPIView.as_view(), name='staff-shift-detail'),
    
    path('staff-attendance/', views.StaffAttandanceListCreateAPIView.as_view(), name='staff-attendance-list-create'),
    path('staff-attendance/<int:pk>/', views.StaffAttandanceRetrieveUpdateDestroyAPIView.as_view(), name='staff-attendance-detail'),
]
