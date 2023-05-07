from django.urls import path
from .views import RoleCreateApiView, RoleRUDApiView, UserRoleCreateApiView, UserRoleRUDApiView, UserCreateApiView, \
    UserRUDApiView


urlpatterns = [
    path('role-create/', RoleCreateApiView.as_view()),
    path('role-rud/<int:pk>/', RoleRUDApiView.as_view()),
    path('user-role-create/', UserRoleCreateApiView.as_view()),
    path('user-role-rud/<int:pk>/', UserRoleRUDApiView.as_view()),
    path('user-create/', UserCreateApiView.as_view()),
    path('user-rud/<int:pk>/', UserRUDApiView.as_view()),
]