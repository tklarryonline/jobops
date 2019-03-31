from django.contrib import admin

from .models import Company, ContactPerson, Job, Stage


class ContactPersonInline(admin.TabularInline):
    model = ContactPerson
    ordering = ('name',)


class StageInline(admin.TabularInline):
    model = Stage
    ordering = ('datetime',)


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'status', 'modified')
    ordering = ('company__name',)
    inlines = [
        StageInline
    ]


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'modified')
    ordering = ('name',)
    inlines = [
        ContactPersonInline
    ]


admin.site.register(Job, JobAdmin)
admin.site.register(Company, CompanyAdmin)
