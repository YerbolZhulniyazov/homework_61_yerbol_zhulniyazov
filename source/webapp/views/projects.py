from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import ProjectForm
from webapp.models import Project


class ProjectCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'projects/project_create.html'
    model = Project
    form_class = ProjectForm
    success_message = 'Проект успешно создан'

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDetail(DetailView):
    template_name = 'projects/project.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = self.object.issues.exclude(is_deleted=True)
        return context


class ProjectUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'projects/project_update.html'
    model = Project
    form_class = ProjectForm
    success_message = 'Проект успешно обновлен'

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'projects/project_confirm_delete.html'
    model = Project
    success_message = 'Проект успешно удален'
    success_url = reverse_lazy('index')
