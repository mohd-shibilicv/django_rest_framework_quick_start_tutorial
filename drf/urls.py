from django.urls import path, include
from rest_framework import routers

from drf.quickstart import views


# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include('snippets.urls')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
