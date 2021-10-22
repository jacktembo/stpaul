from django.urls import path

app_name = 'routine'

from . import staff_views

urlpatterns = [
    path('dashboard/', staff_views.dashboard, name='staff-dashboard'),
    path('assignment/', staff_views.assignment, name='assignment'),
    path('add-assignment/', staff_views.add_assignment, name='add-assignment'),
    path('delete-assignment/<pk>/', staff_views.delete_assignment, name='delete-assignment'),
    path('delete-all-assignments/', staff_views.delete_all_assignments, name='delete-all-assignments'),
    path('edit-assignment/<pk>/', staff_views.edit_assignment, name='edit-assignment'),
    path('resource/', staff_views.resource, name='resource'),
    path('edit-resource/', staff_views.edit_resource, name='edit-resource'),
    path('announcements/', staff_views.announcements, name='staff-announcements'),

]
