from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from webapp.forms import AdForm
from webapp.models import Ad
from webapp.views.search_view import SearchView


class AdListView(SearchView):
    model = Ad
    template_name = 'index.html'
    context_object_name = 'ads'
    ordering = ('-created_at',)
    paginate_by = 3
    paginate_orphans = 0
    search_fields = ["title__icontains", "text__icontains"]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(status='Published').filter(is_deleted=False)
        return queryset


class AdCreateView(LoginRequiredMixin, CreateView):
    model = Ad
    form_class = AdForm
    template_name = 'ad_create.html'

    def form_valid(self, form):
        ad = form.save(commit=False)
        ad.author = self.request.user
        ad.save()
        return redirect('webapp:index')


class AdView(DetailView):
    model = Ad
    context_object_name = 'ad'
    template_name = 'ad_view.html'


class AdDeleteView(PermissionRequiredMixin, DeleteView):
    model = Ad
    context_object_name = 'ad'
    template_name = 'ad_delete.html'
    success_url = reverse_lazy('webapp:index')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.soft_delete()
        messages.success(self.request, f'Объявление: {self.object.title} успешно удален!')
        return HttpResponseRedirect(self.get_success_url())

    def has_permission(self):
        return self.get_object().author == self.request.user


class AdUpdateView(PermissionRequiredMixin, UpdateView):
    model = Ad
    form_class = AdForm
    context_object_name = 'ad'
    template_name = 'ad_create.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(Q(status='Published') & Q(is_deleted=False))
        return queryset

    def has_permission(self):
        return self.get_object().author == self.request.user

    def form_valid(self, form):
        ad = form.save(commit=False)
        ad.status = 'For moderation'
        ad.save()
        return redirect('webapp:index')


class AdReviewListView(PermissionRequiredMixin, SearchView):
    model = Ad
    template_name = 'review.html'
    context_object_name = 'ads'
    ordering = ('-created_at',)
    paginate_by = 3
    paginate_orphans = 0
    search_fields = ["title__icontains", "text__icontains"]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(status='For moderation').filter(is_deleted=False)
        return queryset

    def has_permission(self):
        return self.request.user.is_staff


class AdApproveView(PermissionRequiredMixin, DetailView):
    model = Ad
    template_name = 'ad_approve.html'
    context_object_name = 'ad'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(Q(status='For moderation') & Q(is_deleted=False))
        return queryset

    def has_permission(self):
        return self.request.user.is_staff