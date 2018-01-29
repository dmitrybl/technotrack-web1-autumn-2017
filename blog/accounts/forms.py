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
            elif not user.check_password(password):
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


    def clean_email2(self):
        pa = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already existed")
        return email