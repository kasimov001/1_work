from django.urls import path, include

app_name = 'djob'

urlpatterns = [
    path('api/', include('djob.api.urls')),
]