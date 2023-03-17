from django.urls import path
from webapp.views.base import IndexView, IndexRedirectView
from webapp.views.issues import IssueCreateView, IssueDeleteView, IssueDetailView, IssueUpdateView, IssueIndexView
from webapp.views.projects import ProjectCreate, ProjectDeleteView, ProjectDetail, ProjectUpdate

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('issue/', IndexRedirectView.as_view(), name='redirect'),
    path('issue/<int:pk>', IssueDetailView.as_view(), name='issue_detail'),
    path('issue/<int:pk>/update/', IssueUpdateView.as_view(), name='issue_update'),
    path('issue/<int:pk>/delete/', IssueDeleteView.as_view(), name='issue_delete'),
    path('issue/<int:pk>/confirm_delete/', IssueDeleteView.as_view(), name='issue_confirm_delete'),
    path('project/issues/', IssueIndexView.as_view(), name='issues'),
    path('project/add/', ProjectCreate.as_view(), name='project_add'),
    path('project/<int:pk>/', ProjectDetail.as_view(), name='project_detail'),
    path('project/<int:pk>/update', ProjectUpdate.as_view(), name='project_update'),
    path('project/<int:pk>/issue/add/', IssueCreateView.as_view(), name='add_issue'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('project/<int:pk>/confirm_delete/', ProjectDeleteView.as_view(), name='project_confirm_delete'),
]
