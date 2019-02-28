from django.contrib import admin

from .models import Job


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status')


admin.site.register(Job, JobAdmin)
