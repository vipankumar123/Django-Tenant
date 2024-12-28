from django.contrib import admin
from .models import Task, Tenant
# Register your models here.


admin.site.register(Tenant)
admin.site.register(Task)
