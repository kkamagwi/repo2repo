from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('source_name', 'source_url', 'source_workbench',
                'destination_name', 'destination_url', 'destination_workbench',)

    widgets = {
        'source_name': forms.TextInput(attrs={'class': 'form-control'}),
        'source_url': forms.URLInput(attrs={'class': 'form-control'}),
        'source_workbanch': forms.TextInput(attrs={'class': 'form-control'}),
        'destination_name': forms.TextInput(attrs={'class': 'form-control'}),
        'destination_url': forms.URLInput(attrs={'class': 'form-control'}),
        'destination_workbench': forms.TextInput(attrs={'class': 'form-control'}),
    }


class PushForm(forms.Form):
   pass
        
