from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from backend.trackerr import models

# Register your models here.

admin.site.register(models.User)
admin.site.register(models.Event)
admin.site.register(models.Company)
admin.site.register(models.JobApplication)
admin.site.register(models.CompanyDetail)
