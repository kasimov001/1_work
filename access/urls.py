from django.urls import path, include

app_name = 'access'

urlpatterns = [
    path('access/', include('access.api.urls'))
]