"""PMDesk_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from account import views

from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetCompleteView, logout_then_login, PasswordResetConfirmView

from account.forms import SignInForm, PasswordRemindForm

class Login(LoginView):
    template_name = 'account/sign-in.html'
    authentication_form = SignInForm

class PasswordReset(PasswordResetView):
    template_name = 'account/password-reminder.html'
    # email_template_name = 'account/password-reset-email.html'
    subject_template_name = 'account/password-reset-subject.txt'
    form_class = PasswordRemindForm
    from_email = 'PMDesk'

    html_email_template_name = 'account/password-reset-email.html'


urlpatterns = [
    path('sign-in/', Login.as_view(), name='sign_in'),
    path('sign-out/', logout_then_login, name='sign_out'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-remind/', PasswordReset.as_view(), name='password_reminder'),

]
