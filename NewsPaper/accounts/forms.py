from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="First name")
    last_name = forms.CharField(label="Last name")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        users = Group.objects.get(name="users")
        user.groups.add(users)
        return user
