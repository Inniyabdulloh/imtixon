from . import views
from django.urls import path



urlpatterns = [
    path('home/', views.AttandanceHomeView.as_view(), name="attandance-home"),
]
