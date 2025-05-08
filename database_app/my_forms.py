from django import forms

from database_app.models import Customer


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class CustomerForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')], widget=forms.RadioSelect)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Customer
        fields = ['names', 'email', 'phone', 'pic', 'weight', 'height', 'gender', 'password', 'dob']

#pip install django-crispy-forms
# pip install crispy-bootstrap5
# pip freeze requirements.txt
