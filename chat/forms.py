from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(max_length=128)


class RegistrateForm(forms.Form):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    COLORS = (
        ('black', 'black'),
    )
    username = forms.CharField(min_length=4, max_length=64)
    email = forms.EmailField()
    password = forms.CharField(min_length=8, max_length=128, widget=forms.PasswordInput)
    image = forms.ImageField()
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=GENDERS)
    namecolor = forms.ChoiceField(choices=COLORS)
    information = forms.CharField(max_length=1024)


class MessageForm(forms.Form):
    text = forms.CharField(max_length=1024)
