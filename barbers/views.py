# Imports from django
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
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
        try:
            account_details = AccountDetails.objects.get(
                user = User.objects.get(
                    pk=self.request.user.pk
                )
            )
        except AccountDetails.DoesNotExist:
            raise Http404
        else:
            return account_details

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'username': User.objects.get(pk=self.request.user.pk).username
        })
        return context

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            return redirect(
                reverse(
                    'account_details_create'
                )
            )
        else:
            return super().get(request, *args, **kwargs)


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
        messages.success(
            self.request,
            'Your account has been created!'
        )
        return redirect(self.success_url)


class AccountDetailsCreateView(CreateView):
    form_class = AccountDetailsForm
    template_name = 'account-details-create.html'
    success_url = reverse_lazy('account_details')

    def form_valid(self, form):
        new_account_details = form.save(commit=False)
        new_account_details.user = self.request.user
        new_account_details.save()
        messages.success(
            self.request,
            'Your account details have been created!'
        )
        return redirect(self.success_url)


class UpdateAccountDetailsView(LoginRequiredMixin, UpdateView):
    form_class = AccountDetailsForm
    template_name = 'update-account-details.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        try:
            account_details = AccountDetails.objects.get(
                user=User.objects.get(
                    pk=self.request.user.pk
                )
            )
        except AccountDetails.DoesNotExist:
            raise Http404
        else:
            return account_details

    def get_initial(self):
        initial = super(UpdateAccountDetailsView, self).get_initial()
        return initial

    def get_form_kwargs(self):
        kwargs = super(UpdateAccountDetailsView, self).get_form_kwargs()
        return kwargs

    def form_valid(self, form):
        messages.success(
            self.request,
            'Your account details have been updated!'
        )
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            return redirect(
                reverse(
                    'account_details_create'
                )
            )
        else:
            return super().get(request, *args, **kwargs)

class BarbershopList(ListView):
    model = User
    template_name = 'barbers.html'
    context_object_name = 'barbers'
    queryset = User.objects.all().exclude(queue=None)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            
        })
        return context
