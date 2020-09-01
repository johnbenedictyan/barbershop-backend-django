# Imports from django
from django.contrib.auth import views as auth_views
from django.urls import path

# Imports from foreign installed apps

# Imports from local apps
from .forms import (
    SignInForm, RegisterForm, PasswordChangeForm, PasswordResetForm,
    SetPasswordForm
)
from .views import (
    AccountDetailsView, PasswordChangeDoneRedirectView,
    PasswordResetDoneRedirectView, RegisterView, UpdateAccountDetailsView,
    AccountDetailsCreateView, BarbershopList
)

# Start of Urls

urlpatterns = [
    # Django in-built views urls
    path(
        'password-change/',
        auth_views.PasswordChangeView.as_view(
            template_name='password-change.html',
            form_class=PasswordChangeForm
        ),
        name='password_change'
    ),
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='password-reset.html',
            form_class=PasswordResetForm,
            email_template_name='password-reset-email.html',
            subject_template_name='password-reset-subject.txt'
        ),
        name='password_reset'
    ),
    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='password-reset-done.html',
        ),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='password-reset-confirm.html',
            form_class=PasswordResetForm
        ),
        name='password_reset_confirm'
    ),
    path(
        'sign-in/',
        auth_views.LoginView.as_view(
            template_name='sign-in.html',
            authentication_form=SignInForm
        ),
        name='sign_in'
    ),
    path(
        'sign-out/',
        auth_views.LogoutView.as_view(
            template_name='sign-out.html'
        ),
        name='sign_out'
    ),
    # Custom views urls
    path(
        'details/',
        AccountDetailsView.as_view(),
        name='account_details'
    ),
    path(
        'details/create/',
        AccountDetailsCreateView.as_view(),
        name='account_details_create'
    ),
    path(
        'details/update/',
        UpdateAccountDetailsView.as_view(),
        name='account_details_update'
    ),
    path(
        'password-change/done/',
        PasswordChangeDoneRedirectView.as_view(),
        name='password_change_done'
    ),
    path(
        'reset/done/',
        PasswordResetDoneRedirectView.as_view(),
        name='password_reset_completed'
    ),
    path(
        'register/',
        RegisterView.as_view(),
        name='register'
    ),
    path(
        '',
        BarbershopList.as_view(),
        name='all_barbers'
    )
]
