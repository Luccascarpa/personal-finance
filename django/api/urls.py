from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('personal_finance/', include('personal_finance.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]