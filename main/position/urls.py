from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.PositionHomeView.as_view(), name='position-home'),
    path('create/', views.CreatePositionView.as_view(), name='position-create'),
    path('update/<int:id>/', views.UpdatePositionView.as_view(), name='position-update'),
    path('delete/<int:id>/', views.DeletePositionView.as_view(), name='position-delete'),
]