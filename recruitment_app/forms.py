from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ('name', 'email', 'phone_number', 'country', 'state', 'gender', 'occupation')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adding custom CSS classes to form fields for styling
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            # Adding placeholders for each field
            if field_name == 'name':
                field.widget.attrs['placeholder'] = 'Full name'
            elif field_name == 'email':
                field.widget.attrs['placeholder'] = 'Email'
            elif field_name == 'phone_number':
                field.widget.attrs['placeholder'] = 'Phone number'
            elif field_name == 'country':
                field.widget.attrs['placeholder'] = 'Country'
            elif field_name == 'state':
                field.widget.attrs['placeholder'] = 'State'
            elif field_name == 'gender':
                field.widget.attrs['placeholder'] = 'Gender*'
            elif field_name == 'occupation':
                field.widget.attrs['placeholder'] = 'Occupation type*'

    # Adding labels for each field
    name = forms.CharField(label='Full name')
    email = forms.EmailField(label='Email')
    phone_number = forms.CharField(label='Phone number')
    country = forms.CharField(label='Country')
    state = forms.CharField(label='State')
    gender = forms.ChoiceField(label='Gender*', choices=JobApplication.GENDER_CHOICES)
    occupation = forms.ChoiceField(label='Occupation type*', choices=JobApplication.OCCUPATION_CHOICES)
