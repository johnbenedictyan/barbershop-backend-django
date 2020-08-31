# Imports from django
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

# Imports from foreign installed apps

# Imports from local apps
from .forms import AccountDetailsForm, RegisterForm
from .models import User, AccountDetails

# Start of Views

# Template Views


class AccountDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'account-details.html'
    context_object_name = 'account_details'
    model = AccountDetails

    def get_object(self, queryset=None):
        return AccountDetails.objects.get(
            user=User.objects.get(
                pk=self.request.user.pk
            )
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'username': User.objects.get(pk=self.request.user.pk).username
        })
        return context

# Redirect Views


class PasswordChangeDoneRedirectView(LoginRequiredMixin, RedirectView):
    permanent = True
    pattern_name = 'home'

    def get(self, request, *args, **kwargs):
        messages.success(
            request,
            'Your password has been changed!'
        )
        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)


class PasswordResetDoneRedirectView(LoginRequiredMixin, RedirectView):
    permanent = True
    pattern_name = 'home'

    def get(self, request, *args, **kwargs):
        messages.success(
            request,
            'Your password has been changed!'
        )
        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)

# Form Views


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('sign_in')

    def get_initial(self):
        initial = super(RegisterView, self).get_initial()
        return initial

    def get_form_kwargs(self):
        kwargs = super(RegisterView, self).get_form_kwargs()
        return kwargs

    def form_valid(self, form):
        new_user = form.save()
        new_account_details = AccountDetails(
            user=User.objects.get(pk=new_user.pk)
        )
        new_account_details.save()
        messages.success(
            self.request,
            'Your account has been created!'
        )
        return redirect(self.success_url)


class UpdateAccountDetailsView(LoginRequiredMixin, UpdateView):
    form_class = AccountDetailsForm
    template_name = 'update-account-details.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return AccountDetails.objects.get(
            user=User.objects.get(
                pk=self.request.user.pk
            )
        )

    def get_initial(self):
        initial = super(UpdateAccountDetailsView, self).get_initial()
        return initial

    def get_form_kwargs(self):
        kwargs = super(UpdateAccountDetailsView, self).get_form_kwargs()
        return kwargs

    def form_valid(self, form):
        return super(UpdateAccountDetailsView, self).form_valid(form)

class BarbershopList(ListView):
    model = User
    template_name = 'barbers.html'