from django import forms
from .models import Activity, Applicant
# from .views import calculateAge

import datetime

class DateInput(forms.DateInput):
    input_type = 'date'

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ('name', 'birth_date', 'reg_date', 'activity')
        widgets = {
            'birth_date': DateInput(attrs={'onChange': 'validateDate()', 'id': 'birthdate'}),
            'reg_date': DateInput(attrs={'value': str(datetime.datetime.today().date()), 'onChange': 'validateRegistration()', 'id': 'regdate', 'default': str(datetime.datetime.today().date())}),
            'activity': forms.Select(attrs={'onChange': 'activityChange()', 'name': 'activity'})  
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Applicant Name'
        self.fields['birth_date'].label = 'Birth Date'
        self.fields['reg_date'].label = 'Registration Date'
        self.fields['activity'].label = 'Activity'
        
        
    
    def clean(self):
        super(ApplicantForm, self).clean()
        birth_date = self.cleaned_data.get('birth_date')
        if birth_date > datetime.date.today():
            self._errors['age'] = self.error_class(['Birth date cannot be in the future.'])
        # if calculateAge(birth_date) < 18:
        #     self._errors['age'] = self.error_class(['Applicant must be 18 years or older.'])
        return self.cleaned_data
