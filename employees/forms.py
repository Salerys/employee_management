from django import forms
from .models import PersonalDetails, JobDetails
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True, widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    usable_password = None

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]


class JobDetailsForm(forms.ModelForm):
    class Meta:
        model = JobDetails
        fields = ['department', 'job_position', 'hire_date', 'role']

        widgets = {
            'department': forms.Select(attrs={'class': 'form-control'}),
            'job_position': forms.Select(attrs={'class': 'form-control'}),
            'hire_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'role': forms.Select(attrs={'class': 'form-control'}),
        }


class EditProfileForm(forms.ModelForm):
    phone_number = forms.CharField(widget=forms.NumberInput)
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'id': 'new-password'}),
    )
    confirm_new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'id': 'confirm-new-password'}),
    )

    class Meta:
        model = PersonalDetails
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'phone_number',
        ]

        # Override the form to set required=False for every field

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_new_password = cleaned_data.get('confirm_new_password')

        # Check if the new passwords match
        if new_password and new_password != confirm_new_password:
            self.add_error('confirm_new_password', 'Passwords do not match.')


class EditEmployeeForm(forms.ModelForm):
    review_date = forms.DateField(
        required=False, widget=forms.DateInput(attrs={'type': 'date'})
    )
    rating = forms.IntegerField(required=False, min_value=1, max_value=5)
    comments = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = JobDetails
        fields = ['department', 'job_position', 'hire_date', 'role']
        widgets = {
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        # Capture the current user's role (passed from the view)
        current_user_role = kwargs.pop('current_user_role', None)
        super().__init__(*args, **kwargs)

        # Dynamically filter the role choices
        if current_user_role != 'ADM':  # Non-admin users
            self.fields['role'].choices = [
                choice for choice in JobDetails.ROLE_CHOICES if choice[0] != 'ADM'
            ]
