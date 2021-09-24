from django.urls import path

app_name = 'routine'

from . import staff_views

urlpatterns = [
    path('dashboard/', staff_views.dashboard, name='staff-dashboard'),
    path('add-assignment/', staff_views.add_assignment, name='add-assignment'),

]
