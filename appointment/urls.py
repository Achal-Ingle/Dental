from django.urls import path
from .views import make_appointment, appointment_success

urlpatterns = [
    path('appointment/', make_appointment, name='make_appointment'),
    path('appointment/success/', appointment_success, name='appointment_success'),
]