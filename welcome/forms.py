from django import forms
# from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Row, Layout, Submit
from crispy_forms.bootstrap import FormActions




class LoginForm(forms.Form):
    '''Form for user login'''

    username = forms.CharField(
        label='Username',
        max_length=50,
        widget=forms.TextInput(attrs={'autocomplete': 'username'})
    )
    password = forms.CharField(
        label='Password',
        max_length=50,
        widget=forms.PasswordInput(attrs={'autocomplete': 'password'})
    )

    helper = FormHelper()
    helper.form_id = 'login-form'
    helper.layout = Layout(
        Row('username', css_class="mb-2"),
        Row('password', css_class="mb-2"),
        FormActions(
            Submit('login', 'Log in', css_class="mt-2"),
        )
    )


class RegisterForm(forms.Form):
    '''Form for user signup'''

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'username',
            }
        )
    )
    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'First Name',
            }
        )
    )
    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'Last Name',
            }
        )
    )
    dob = forms.CharField(
        label='dob',
        widget=forms.DateInput(
            format=('%Y-%m-%d'),
            attrs={
                'autocomplete': 'Date Of Birth',
                'type': 'date',
            }
        )
    )
    email = forms.CharField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'autocomplete': 'Email',
            }
        )
    )
    password = forms.CharField(
        label='Password',
        max_length=50,
        widget=forms.PasswordInput(attrs={'autocomplete': 'password'})
    )
    password_confirm = forms.CharField(
        label='Confirm Password',
        max_length=50,
        widget=forms.PasswordInput,
    )

    helper = FormHelper()
    helper.form_id = 'register-form'
    helper.layout = Layout(
        Row('username', css_class='mb-2'),
        Row('first_name', css_class='mb-2'),
        Row('last_name', css_class='mb-2'),
        Row('dob', css_class='mb-2'),
        Row('email', css_class='mb-2'),
        Row('password', css_class='mb-2'),
        Row('password_confirm', css_class='mb-2'),
        FormActions(
            Submit('register', 'Register', css_class="btn-primary"),
            css_class='mt-3'
        )
    )
    
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
