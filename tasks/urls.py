from django.conf.urls import url, include
from . import views
app_name = 'tasks'

urlpatterns = [
    # /tasks/
    url(r'^$', views.IndexView.as_view(), name='home'),

    url(r'^add-task/$', views.TaskCreate.as_view(), name='add-task'),
    url(r'^(?P<pk>[0-9]+)/delete$', views.TaskDelete.as_view(), name='task-delete'),
    url(r'^(?P<pk>[0-9]+)/status$', views.TaskStatusUpdate.as_view(), name='status-update'),
    url(r'^(?P<pk>[0-9]+)/$', views.TaskUpdate.as_view(), name='task-update'),
]

