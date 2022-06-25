from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse

from django.views.generic import CreateView, DetailView

from accounts.forms import MyUserCreationForm
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

    # def get_context_data(self, **kwargs):
    #     if self.get_object() == self.request.user:
    #         kwargs['photos'] = self.get_object().photos.all()
    #         kwargs['albums'] = self.get_object().album.all()
    #     else:
    #         kwargs['photos'] = self.get_object().photos.filter(is_private=False)
    #         kwargs['albums'] = self.get_object().album.filter(is_private=False)
    #     return super().get_context_data(**kwargs)
