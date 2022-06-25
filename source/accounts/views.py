from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator
from django.urls import reverse

from django.views.generic import CreateView, DetailView, UpdateView

from accounts.forms import MyUserCreationForm, ProfileUpdateForm
from accounts.models import Users


class RegisterView(CreateView):
    model = Users
    template_name = 'registration/registration.html'
    form_class = MyUserCreationForm

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('webapp:index')
        return next_url


class UserProfileView(DetailView):
    model = Users
    template_name = 'registration/profile.html'
    context_object_name = "user_object"
    paginate_related_by = 3
    paginate_related_orphans = 0

    def get_context_data(self, **kwargs):
        if self.get_object() == self.request.user:
            ads = self.get_object().ads.exclude(is_deleted=True)
        else:
            ads = self.get_object().ads.filter(status='Published')
        paginator = Paginator(
            ads,
            self.paginate_related_by,
            self.paginate_related_orphans,
            )
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        kwargs['page_obj'] = page
        kwargs['ads'] = page.object_list
        kwargs['is_paginated'] = page.has_other_pages()
        return super().get_context_data(**kwargs)


class UserUpdateView(PermissionRequiredMixin, UpdateView):
    model = Users
    template_name = 'profile_update.html'
    context_object_name = 'user_obj'
    form_class = ProfileUpdateForm

    def has_permission(self):
        return self.get_object() == self.request.user

    def get_success_url(self):
        return reverse('accounts:user_profile', kwargs={'pk': self.request.user.id})