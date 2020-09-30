# Imports from django
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, UserCreationForm,
    SetPasswordForm
)

# Imports from foreign installed apps
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

# Imports from local apps
from .models import AccountDetails

# Start of Forms

# Forms that inherit from inbuilt Django forms


class PasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column(
                    'old_password',
                    css_class='form-group col-12'
                ),
                css_class='form-row'
            ),
            Row(
                Column(
                    'new_password1',
                    css_class='form-group col-12'
                ),
                css_class='form-row'
            ),
            Row(
                Column(
                    'new_password2',
                    css_class='form-group col-12'
                ),
                css_class='form-row'
            ),
            Row(
                Column(
                    Submit(
                        'submit',
                        'Change Password',
                        css_class="btn btn-primary w-50"
                    ),
                    css_class='form-group col-12 text-center'
                ),
                css_class='form-row'
            ),
        )


class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column(
                    'email',
                    css_class='form-group col-12'
                ),
                css_class='form-row'
            ),
            Row(
                Column(
                    Submit(
                        'submit',
                        'Reset Password',
                        css_class="btn btn-primary w-50"
                    ),
                    css_class='form-group col-12 text-center'
                ),
                css_class='form-row'
            ),
        )


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'password1',
            'password2'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column(
                    'username',
                    css_class='form-group'
                ),
                css_class='form-row'
            ),
            Row(
                Column(
                    'password1',
                    css_class='form-group col-md-6'
                ),
                Column(
                    'password2',
                    css_class='form-group col-md-6'
                ),
                css_class='form-row'
            ),
            Row(
                Column(
                    Submit(
                        'submit',
                        'Create an Account',
                        css_class="btn btn-primary w-50"
                    ),
                    css_class='form-group col-12 text-center'
                ),
                css_class='form-row'
            ),
        )


class SetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column(
                    'new_password1',
                    css_class='form-group col-md-6'
                ),
                Column(
                    'new_password2',
                    css_class='form-group col-md-6'
                ),
                css_class='form-row'
            ),
            Row(
                Column(
                    Submit(
                        'submit',
                        'Reset Password',
                        css_class="btn btn-primary w-50"
                    ),
                    css_class='form-group col-12 text-center'
                ),
                css_class='form-row'
            ),
        )


class SignInForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column(
                    'username',
                    css_class='form-group col-12'
                ),
                css_class='form-row'
            ),
            Row(
                Column(
                    'password',
                    css_class='form-group col-12'
                ),
                css_class='form-row'
            ),
            Row(
                Column(
                    Submit(
                        'submit',
                        'Sign In',
                        css_class="btn btn-primary w-50"
                    ),
                    css_class='form-group col-12 text-center'
                ),
                css_class='form-row'
            ),
        )

# Model Forms


class AccountDetailsForm(forms.ModelForm):
    class Meta:
        model = AccountDetails
        exclude = ['user','uuid']
        widgets = {
            'address_1': forms.TextInput(
                attrs={
                    'placeholder': 'Street address'
                }
            ),
            'address_2': forms.TextInput(
                attrs={
                    'placeholder': 'Unit Number (optional)'
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column(
                    'name',
                    css_class='form-group'
                ),
                css_class='form-row'
            ),
            Row(
                Column(
                    'address_1',
                    css_class='form-group col-md-4'
                ),
                Column(
                    'address_2',
                    css_class='form-group col-md-4'
                ),
                Column(
                    'postal_code',
                    css_class='form-group col-md-4'
                ),
                css_class='form-row'
            ),
            Row(
                Column(
                    'email',
                    css_class='form-group col-md-6'
                ),
                Column(
                    'phone',
                    css_class='form-group col-md-6'
                ),
                css_class='form-row'
            ),
            Row(
                Column(
                    Submit(
                        'submit',
                        'Submit',
                        css_class="btn btn-primary w-75"
                    ),
                    css_class='form-group col-12 text-center'
                ),
                css_class='form-row'
            ),
        )

# Generic Forms (forms.Form)
