
from django.urls import path,include
from employees.api import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('emp', views.EmployeeModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]