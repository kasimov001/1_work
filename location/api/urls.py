from django.urls import path
from .views import RegionCreateApiView, RegionRUDApiView, DistrictCreateApiView, DistrictRUDApiView

urlpatterns = [
    path('region-create/', RegionCreateApiView.as_view()),
    path('region-rud/<int:pk>/', RegionRUDApiView.as_view()),
    path('district-create/', DistrictCreateApiView.as_view()),
    path('district-rud/<int:pk>/', DistrictRUDApiView.as_view()),
]