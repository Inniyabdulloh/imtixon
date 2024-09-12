from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.ShiftHomeView.as_view(), name='shift-home'),
    path('create/', views.CreateShiftView.as_view(), name='shift-create'),
    path('update/<int:id>/', views.UpdateShiftView.as_view(), name='shift-update'),
    path('delete/<int:id>/', views.DeleteShiftView.as_view(), name='shift-delete')
]