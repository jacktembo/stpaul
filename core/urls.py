# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

admin.AdminSite.site_header = "ST Paul's College Of Nursing & Midwifery"
admin.AdminSite.site_title = "ST Paul's College | Administration"
admin.AdminSite.index_title = 'College Administration'


urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("", include("apps.home.urls"))             # UI Kits Html files
]
