from django import forms
from .models import Services

class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['assigne_to', 'service_description', 'amount', 'quantity']
        widgets = {
            'assigne_to': forms.Select(attrs={'class': 'form-select'}),
            'service_description': forms.TextInput(attrs={'class': 'form-control border'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control border', 'step': '0.01'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control border', 'step': '1'}),
        }

# class ServicesForm(forms.ModelForm):
#     class Meta:
#         model = Services
#         fields = '__all__'  # Include all fields

#     def __init__(self, *args, **kwargs):
#         super(ServicesForm, self).__init__(*args, **kwargs)
#         for field in self.fields:
#             # Add basic MDB form attributes
#             self.fields[field].widget.attrs.update({
#                 'class': 'form-control'
#             })
#             # Add specific MDB attributes for some fields (optional)
#             if field == 'assigne_to':
#                 self.fields[field].widget.attrs.update({
#                     'mdb_select': True,  # For dropdown selection
#                 })
#             if field == 'amount':
#                 self.fields[field].widget.attrs.update({
#                     'type': 'number',  # For number input
#                 })
