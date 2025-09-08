# dispositivos/management/commands/seed_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta
import random
from decimal import Decimal

from dispositivos.models import Organization, Category, Zone, Device, Measurement, Alert


class Command(BaseCommand):
    help = 'Populate database with sample data for evaluation'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting data seed...'))
        
        # Crear usuario demo si no existe
        user, created = User.objects.get_or_create(
            username='demo_user',
            defaults={
                'email': 'demo@ecoenergy.com',
                'first_name': 'Demo',
                'last_name': 'User'
            }
        )
        
        # Crear organización demo
        org, created = Organization.objects.get_or_create(
            email='demo@ecoenergy.com',
            defaults={
                'name': 'EcoEnergy Demo Company',
            }
        )
        self.stdout.write(f'Organization: {org.name}')
        
        # Crear categorías
        categories_data = [
            {'name': 'Solar Panels', 'description': 'Solar energy devices'},
            {'name': 'Wind Turbines', 'description': 'Wind energy generators'},
            {'name': 'Battery Storage', 'description': 'Energy storage systems'},
            {'name': 'Smart Meters', 'description': 'Energy monitoring devices'},
        ]
        
        categories = []
        for cat_data in categories_data:
            cat, created = Category.objects.get_or_create(
                name=cat_data['name'],
                organization=org,
                defaults={'description': cat_data['description']}
            )
            categories.append(cat)
            self.stdout.write(f'Category: {cat.name}')
        
        # Crear zonas
        zones_data = [
            {'name': 'Building A', 'location': 'Main Campus', 'max_capacity': Decimal('150.00')},
            {'name': 'Building B', 'location': 'North Wing', 'max_capacity': Decimal('200.00')},
            {'name': 'Parking Lot', 'location': 'Outdoor Area', 'max_capacity': Decimal('75.00')},
            {'name': 'Roof Area', 'location': 'Building Top', 'max_capacity': Decimal('300.00')},
        ]
        
        zones = []
        for zone_data in zones_data:
            zone, created = Zone.objects.get_or_create(
                name=zone_data['name'],
                organization=org,
                defaults={
                    'location': zone_data['location'],
                    'max_capacity': zone_data['max_capacity'],
                    'description': f"Zone located at {zone_data['location']}"
                }
            )
            zones.append(zone)
            self.stdout.write(f'Zone: {zone.name}')
        
        # Crear dispositivos
        devices_data = [
            {'name': 'Solar Panel Unit 1', 'model': 'SP-300W', 'power_watts': 300, 'category': 0, 'zone': 3},
            {'name': 'Solar Panel Unit 2', 'model': 'SP-300W', 'power_watts': 300, 'category': 0, 'zone': 3},
            {'name': 'Wind Generator A', 'model': 'WG-5KW', 'power_watts': 5000, 'category': 1, 'zone': 2},
            {'name': 'Battery Pack 1', 'model': 'BP-Tesla-100', 'power_watts': 1000, 'category': 2, 'zone': 0},
            {'name': 'Smart Meter Main', 'model': 'SM-Advanced', 'power_watts': 50, 'category': 3, 'zone': 0},
            {'name': 'Smart Meter B-Wing', 'model': 'SM-Standard', 'power_watts': 50, 'category': 3, 'zone': 1},
            {'name': 'Solar Panel Unit 3', 'model': 'SP-400W', 'power_watts': 400, 'category': 0, 'zone': 3},
            {'name': 'Battery Pack 2', 'model': 'BP-Tesla-150', 'power_watts': 1500, 'category': 2, 'zone': 1},
        ]
        
        devices = []
        for dev_data in devices_data:
            device, created = Device.objects.get_or_create(
                name=dev_data['name'],
                organization=org,
                defaults={
                    'model': dev_data['model'],
                    'power_watts': dev_data['power_watts'],
                    'category': categories[dev_data['category']],
                    'zone': zones[dev_data['zone']],
                    'consumption': random.randint(50, dev_data['power_watts']),
                    'status': random.choice(['active', 'active', 'active', 'inactive'])  # Mostly active
                }
            )
            devices.append(device)
            self.stdout.write(f'Device: {device.name}')
        
        # Crear mediciones (últimas 2 semanas)
        self.stdout.write('Creating measurements...')
        start_date = timezone.now() - timedelta(days=14)
        
        for device in devices:
            # Crear mediciones cada 2-6 horas
            current_time = start_date
            while current_time <= timezone.now():
                consumption = Decimal(str(random.uniform(0.5, 15.0)))  # Entre 0.5 y 15 kWh
                
                Measurement.objects.create(
                    organization=org,
                    device=device,
                    consumption_kwh=consumption,
                    timestamp=current_time
                )
                
                # Siguiente medición en 2-6 horas
                current_time += timedelta(hours=random.randint(2, 6))
        
        self.stdout.write(f'Created measurements for {len(devices)} devices')
        
        # Crear alertas de la semana
        self.stdout.write('Creating alerts...')
        week_ago = timezone.now() - timedelta(days=7)
        
        alerts_data = [
            {'device': 0, 'type': 'high_consumption', 'severity': 'grave', 'message': 'Critical: Solar Panel Unit 1 consuming excessive energy'},
            {'device': 2, 'type': 'device_offline', 'severity': 'alta', 'message': 'Wind Generator A is offline'},
            {'device': 1, 'type': 'high_consumption', 'severity': 'media', 'message': 'Solar Panel Unit 2 consumption above normal'},
            {'device': 3, 'type': 'zone_limit_exceeded', 'severity': 'alta', 'message': 'Battery Pack 1 zone limit exceeded'},
            {'device': 4, 'type': 'high_consumption', 'severity': 'media', 'message': 'Smart Meter showing irregular readings'},
            {'device': 6, 'type': 'high_consumption', 'severity': 'grave', 'message': 'Solar Panel Unit 3 critical consumption detected'},
        ]
        
        for alert_data in alerts_data:
            Alert.objects.create(
                organization=org,
                device=devices[alert_data['device']],
                alert_type=alert_data['type'],
                severity=alert_data['severity'],
                message=alert_data['message'],
                alert_date=week_ago + timedelta(days=random.randint(0, 7), hours=random.randint(0, 23))
            )
        
        self.stdout.write(f'Created {len(alerts_data)} alerts')
        
        # Estadísticas finales
        self.stdout.write(self.style.SUCCESS('\n=== DATA SEED COMPLETED ==='))
        self.stdout.write(f'Organizations: {Organization.objects.count()}')
        self.stdout.write(f'Categories: {Category.objects.count()}')
        self.stdout.write(f'Zones: {Zone.objects.count()}')
        self.stdout.write(f'Devices: {Device.objects.count()}')
        self.stdout.write(f'Measurements: {Measurement.objects.count()}')
        self.stdout.write(f'Alerts: {Alert.objects.count()}')
        self.stdout.write(self.style.SUCCESS('Ready for demo!'))