from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

    # cleaning a field data manually
    # or setting our own validation fields
    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get('email')
    #     print(email)
    #     if email.endswith(".edu"):
    #         raise forms.ValidationError("this is not a valid email. Please dont use .edu")
    #     return email

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
