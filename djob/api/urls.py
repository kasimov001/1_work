from django.urls import path, include
from .views import CategoryCreateApiView, CategoryRUDApiView, JobCreateApiView, JobRUDApiView, WorkerCreateApiView, WorkerRUDApiView

urlpatterns = [
    path('category-create/', CategoryCreateApiView.as_view()),
    path('category-rud/<int:pk>/', CategoryRUDApiView.as_view()),
    path('job-create/', JobCreateApiView.as_view()),
    path('job-rud/<int:pk>/', JobRUDApiView.as_view()),
    path('worker-create/', WorkerCreateApiView.as_view()),
    path('worker-rud/<int:pk>/', WorkerRUDApiView.as_view()),
]