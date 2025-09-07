from django.contrib import admin
from .models import Organization, Category, Zone, Device, Measurement, Alert

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    search_fields = ['name', 'email']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'organization', 'created_at']
    search_fields = ['name']
    list_filter = ['organization']

@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'max_capacity', 'organization', 'created_at']
    search_fields = ['name', 'location']
    list_filter = ['organization']

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'model', 'category', 'zone', 'status', 'power_watts', 'organization']
    list_filter = ['category', 'zone', 'status', 'organization']
    search_fields = ['name', 'model']

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['device', 'consumption_kwh', 'timestamp', 'organization']
    list_filter = ['timestamp', 'device__category', 'organization']
    search_fields = ['device__name']

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ['device', 'alert_type', 'severity', 'status', 'alert_date', 'organization']
    list_filter = ['alert_type', 'severity', 'status', 'alert_date', 'organization']
    search_fields = ['device__name', 'message']