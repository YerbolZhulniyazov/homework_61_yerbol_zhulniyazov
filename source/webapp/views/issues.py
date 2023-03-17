from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from webapp.forms import IssueForm, SearchForm
from webapp.models import Issue, Project


class IssueIndexView(ListView):
    template_name = 'issues/issue_index.html'
    model = Issue
    context_object_name = 'issues'
    ordering = ('-created_at',)
    paginate_by = 10
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)
        if self.search_value:
            query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context


class IssueCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Issue
    form_class = IssueForm
    template_name = 'issues/add_issue.html'
    success_message = 'Задача создана'

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        issue = form.save(commit=False)
        issue.project = project
        issue.save()
        return redirect('/')


class IssueDetailView(DetailView):
    template_name = 'issues/issue_detail.html'
    model = Issue


class IssueUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Issue
    form_class = IssueForm
    template_name = 'issues/issue_update.html'
    success_message = 'Задача успешно обновлена'

    def get_success_url(self):
        return reverse('issue_detail', kwargs={'pk': self.object.pk})


class IssueDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'issues/issue_confirm_delete.html'
    model = Issue
    success_message = 'Задача успшено удалена'
    success_url = reverse_lazy('index')
