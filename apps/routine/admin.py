from django.contrib import admin

from apps.routine.models import Student, Program, Lecturer, TargetAudience, Announcement

admin.site.register(Student)
admin.site.register(Program)
admin.site.register(Lecturer)
admin.site.register(Announcement)
