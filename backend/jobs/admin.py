from django.contrib import admin

from .models import Company, Job


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'status')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Job, JobAdmin)
admin.site.register(Company, CompanyAdmin)
