from django.urls import path
from .views import ProjectImageUploadView


urlpatterns = [
    path('', ProjectImageUploadView.as_view()),

]
