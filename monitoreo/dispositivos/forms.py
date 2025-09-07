from django import forms
from .models import Device, Category, Zone, Organization

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'model', 'category', 'zone', 'status', 'power_watts', 'consumption']
    
    def __init__(self, *args, **kwargs):
        organization = kwargs.pop('organization', None)
        super().__init__(*args, **kwargs)
        
        # Filtrar categorías y zonas por organización
        if organization:
            self.fields['category'].queryset = Category.objects.filter(organization=organization)
            self.fields['zone'].queryset = Zone.objects.filter(organization=organization)
        else:
            # Temporal: usar la primera organización
            first_org = Organization.objects.first()
            if first_org:
                self.fields['category'].queryset = Category.objects.filter(organization=first_org)
                self.fields['zone'].queryset = Zone.objects.filter(organization=first_org)
    
    # Validación personalizada
    def clean_power_watts(self):
        power = self.cleaned_data['power_watts']
        if power <= 0:
            raise forms.ValidationError("Power must be greater than zero")
        return power
    
    def clean_consumption(self):
        consumption = self.cleaned_data['consumption']
        if consumption < 0:
            raise forms.ValidationError("Consumption cannot be negative")
        return consumption

# Formulario para filtros
class DeviceFilterForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=Category.objects.none(),
        required=False,
        empty_label="All Categories"
    )
    
    def __init__(self, *args, **kwargs):
        organization = kwargs.pop('organization', None)
        super().__init__(*args, **kwargs)
        
        if organization:
            self.fields['category'].queryset = Category.objects.filter(organization=organization)
        else:
            # Temporal: usar la primera organización
            first_org = Organization.objects.first()
            if first_org:
                self.fields['category'].queryset = Category.objects.filter(organization=first_org)