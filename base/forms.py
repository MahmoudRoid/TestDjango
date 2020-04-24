from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from base.models import Member


class SignupForm(UserCreationForm):  # az in class ers borde chon mikhastim login konim hash shode ro mikhast ke nadashtim ==> in class handle mikone password ro khodesh

    agreement = forms.BooleanField(required=False)

    class Meta:
        model = Member
        fields = ('first_name','last_name','username','email','image')

    def clean_agreement(self):
        data = self.cleaned_data['agreement'];
        if not data:
            raise ValidationError('You should accept rules')
        return data


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True , widget=forms.PasswordInput)
