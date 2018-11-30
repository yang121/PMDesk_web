from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, UsernameField
from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, PasswordInput, CharField, EmailField
from django.utils.translation import gettext, gettext_lazy as _


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        # label=_("Password"),
        strip=False,
        widget=PasswordInput(attrs={"placeholder": "输入密码", "class": "form-control"}),
        help_text=password_validation.password_validators_help_text_html(),
        error_messages={'required': '请填写密码', 'invalid': '密码格式错误'}
    )
    password2 = forms.CharField(
        # label=_("Password confirmation"),
        widget=PasswordInput(attrs={"placeholder": "再次输入密码", "class": "form-control"}),
        strip=False,
        # help_text=_("Enter the same password as before, for verification."),
        error_messages={'required': '请再次输入密码，确保无误','password_mismatch': _("两次输入的密码不一致.")}
    )


    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        field_classes = {'username': UsernameField}
        widgets = {
            'username': TextInput(attrs={'autofocus': True, "placeholder": "用户名", "class": "form-control"}),
            'email': EmailInput(attrs={"placeholder": "电子邮箱", "class": "form-control"}),
        }
        error_messages = {
            'username': {'required': '请填写用户名', 'invalid': '用户名格式错误'},
            'email': {'required': '请填写电子邮箱', 'invalid': '邮箱格式错误'},
        }


class SignInForm(AuthenticationForm):
    username = UsernameField(
        max_length=254,
        widget=TextInput(attrs={'autofocus': True, "placeholder": "用户名", "class": "form-control"}),
        error_messages={'required': '请填写用户名', 'invalid': '用户名格式错误'},
        required=True
    )
    password = CharField(
        strip=False,
        widget=PasswordInput(
            attrs={"placeholder": "密码", "class": "form-control"}
        ),
        error_messages={'required': '请填写密码', 'invalid': '密码格式错误'}
    )

    error_messages = {
        'invalid_login': _(
            "请输入正确的%(username)s或密码。注意区分大小写" % {'username': '用户名'}
        ),
        'inactive': _("此账户未激活."),
        # 'password_mismatch': _("此用户名已被注册."),
    }


class PasswordRemindForm(PasswordResetForm):
    email = EmailField(
        max_length=254,
        widget=EmailInput(attrs={'autofocus': True, 'class': 'form-control', 'placeholder': 'Email'}),
        required=True
    )

