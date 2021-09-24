# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

import apps.StudentsAccounts.views as accounts_views
import apps.routine.views as routine_views

admin.AdminSite.site_header = "ST Paul's College Of Nursing & Midwifery"
admin.AdminSite.site_title = "ST Paul's College | Administration"
admin.AdminSite.index_title = 'College Administration'


urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("staff/accounts/", include("apps.StaffAccounts.urls")), # Auth routes - login / register
    path("staff/home", include("apps.home.urls")),         # UI Kits Html files
    path('', accounts_views.login_view),
    path('students/accounts/', include("apps.StudentsAccounts.urls")),

]
