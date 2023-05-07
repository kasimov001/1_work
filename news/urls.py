from django.urls import path, include

app_name = 'news'

urlpatterns = [
    path('api/', include('news.api.urls'))
]