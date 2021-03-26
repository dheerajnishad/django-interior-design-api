from django.urls import path
from Project import views

urlpatterns = [
    path('', views.project_all, name='project'),
    path('<uuid:pk>', views.project_by_id, name='projectById'),

]