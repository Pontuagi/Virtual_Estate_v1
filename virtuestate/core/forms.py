from django import forms

class PropertySearchForm(forms.Form):
    property_type = forms.ChoiceField(label='Property Type', choices=[('all', 'All'), ('apartment', 'Apartment'), ('house', 'House'), ('villa', 'Villa')])
    number_of_rooms = forms.IntegerField(label='Number of Rooms', min_value=1, required=False)
    min_price = forms.IntegerField(label='Minimum Price', min_value=0, required=False)
    max_price = forms.IntegerField(label='Maximum Price', min_value=0, required=False)