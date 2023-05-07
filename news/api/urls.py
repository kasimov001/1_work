from django.urls import path
from .views import NewCreateApiView, NewRUDApiView

urlpatterns = [
    path('new-create/', NewCreateApiView.as_view()),
    path('new/rud/<int:pk>/', NewRUDApiView.as_view()),
]