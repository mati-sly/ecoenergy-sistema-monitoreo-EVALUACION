from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid

# Organization model - required by evaluation
class Organization(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Zone(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='zones')
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=200)
    max_capacity = models.DecimalField(max_digits=10, decimal_places=2, help_text="Maximum capacity in kW")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.location}"

class Device(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('maintenance', 'Under Maintenance'),
    ]
    
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='devices')
    name = models.CharField(max_length=150)
    model = models.CharField(max_length=100)
    power_watts = models.PositiveIntegerField(help_text="Power in watts")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='devices')
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name='devices')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    consumption = models.IntegerField(help_text="Current consumption in watts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.model}) - {self.zone.name}"
    
    class Meta:
        unique_together = ['name', 'zone']

class Measurement(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='measurements')
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='measurements')
    consumption_kwh = models.DecimalField(max_digits=10, decimal_places=3)
    timestamp = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.device.name} - {self.consumption_kwh} kWh"
    
    class Meta:
        verbose_name_plural = "Measurements"
        ordering = ['-timestamp']

class Alert(models.Model):
    TYPE_CHOICES = [
        ('high_consumption', 'High Consumption'),
        ('device_offline', 'Device Offline'),
        ('zone_limit_exceeded', 'Zone Limit Exceeded'),
    ]
    
    SEVERITY_CHOICES = [
        ('Mediano', 'Mediano'),
        ('Alto', 'Alto'), 
        ('Grave', 'Grave'),
    ]
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('resolved', 'Resolved'),
        ('dismissed', 'Dismissed'),
    ]
    
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='alerts')
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='alerts')
    alert_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    message = models.TextField()
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    alert_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Alert {self.severity} - {self.device.name}"
    
    class Meta:
        ordering = ['-alert_date']

class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)  # Cambiado de UUID a código de 6 dígitos
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    used = models.BooleanField(default=False)
    
    def is_valid(self):
        # Código válido por 10 minutos
        return not self.used and (timezone.now() - self.created_at).total_seconds() < 600
    
    def __str__(self):
        return f"Code {self.code} for {self.user.email} - {'Used' if self.used else 'Active'}"
    
    class Meta:
        ordering = ['-created_at']