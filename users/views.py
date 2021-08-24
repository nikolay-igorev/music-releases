from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db import IntegrityError

from .forms import CustomUserCreationForm, EditProfileForm, CreateCurrencyForm, LabelForm
from .models import Profile, ProfileCurrency, Label, Invitation
from django.core.exceptions import PermissionDenied


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        invitation = Invitation.objects.filter(uuid=self.kwargs['uuid'])
        if invitation.exists():
            if invitation[0].active:
                return super(SignUpView, self).dispatch(request, *args, **kwargs)

        raise PermissionDenied

    def form_valid(self, form):

        valid = super(SignUpView, self).form_valid(form)
        if valid:
            invitation = Invitation.objects.get(uuid=self.kwargs['uuid'])
            invitation.active = False
            invitation.save()

        return valid


class ShowInvitationsView(ListView):
    model = Invitation
    template_name = "invitation.html"
    context_object_name = "invitations"

    def get_queryset(self):
        return super().get_queryset().filter(profile=self.request.user.profile)


class EditProfileView(UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'profile_edit.html'
    success_url = reverse_lazy('profile_edit')

    def get_object(self, queryset=None):
        return self.request.user.profile


class CreateProfileCurrencyView(CreateView):
    model = ProfileCurrency
    fields = ['currency']
    success_url = reverse_lazy('currencies_list')

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        try:
            return super().form_valid(form)
        except IntegrityError:
            messages.error(self.request, 'You have already chosen that currency')
            return redirect('currencies_list')


class ListProfileCurrencyView(ListView):
    model = ProfileCurrency
    template_name = 'currencies_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(profile=self.request.user.profile)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreateCurrencyForm(self.request.user.profile)
        return context


class DeleteProfileCurrencyView(DeleteView):
    model = ProfileCurrency
    success_url = reverse_lazy('currencies_list')


class CreateLabelView(CreateView):
    model = Label
    form_class = LabelForm
    template_name = 'label_add.html'
    success_url = reverse_lazy('labels_list')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        try:
            return super().form_valid(form)
        except IntegrityError:
            form.add_error('name', "You already have this label")
            return super().form_invalid(form)

    def get_success_url(self):
        pass


class ListLabelView(ListView):
    model = Label
    context_object_name = 'labels'
    template_name = 'labels_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(profile=self.request.user.profile)


class UpdateLabelView(UpdateView):
    model = Label
    context_object_name = 'label'
    template_name = 'label_update.html'
    form_class = LabelForm
    success_url = reverse_lazy('labels_list')

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError:
            form.add_error('name', "You already have this label")
            return super().form_invalid(form)


class DeleteLabelView(DeleteView):
    model = Label
    context_object_name = 'label'
    template_name = 'label_delete.html'
    success_url = reverse_lazy('labels_list')
