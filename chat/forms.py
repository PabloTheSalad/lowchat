from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(max_length=128)


class RegistrateForm(forms.Form):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    username = forms.CharField(min_length=4, max_length=64)
    email = forms.EmailField()
    password = forms.CharField(min_length=8, max_length=128, widget=forms.PasswordInput)
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=GENDERS)
    namecolor = forms.CharField(max_length=32)
    information = forms.CharField(max_length=1024)


class MessageForm(forms.Form):
    text = forms.CharField(max_length=1024)
