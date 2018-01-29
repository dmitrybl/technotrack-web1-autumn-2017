from django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            user_qs = User.objects.filter(username=username)
            if not user_qs.exists():
                raise forms.ValidationError("User doesn't exists!")
            if not user:
                raise forms.ValidationError("Wrong login or password!")
            if not user.check_password(password):
                raise forms.ValidationError("Wrong login or password!")

        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password2'
        ]


    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if username and password and password2:
            user_qs = User.objects.filter(username=username)
            if user_qs.exists():
                raise forms.ValidationError("Such user already exists!")
            if password != password2:
                raise forms.ValidationError("Passwords must match")

        return super(UserRegisterForm, self).clean(*args, **kwargs)