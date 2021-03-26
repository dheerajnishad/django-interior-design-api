from django.urls import path
from Category import views

urlpatterns = [
    path('', views.category_all, name='Category'),
    path('<uuid:pk>', views.category_by_id, name='categoryById'),
    ]