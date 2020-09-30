"""Django_To_Restapi_CBV_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include

from employees import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # our django app cbv urls
    path('employee/', views.EmployeeListView.as_view(), name='employee_list'),
    path('employee/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('employee/create/', views.EmployeeCreateView.as_view(), name='employee_create'),

    path('employee/<int:pk>/update/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete'),



    # our django application rest-api urls
    path('api/', include('employees.api.urls')),














    # Provider app communication urls
    path('contacts/', views.ContactListView,name='contacts'),



    path('contacts/detail/<int:pk>/', views.ContactDetailView,name='contacts_detail'),




    path('contacts/delete/<int:pk>/', views.ContactDeleteView,name='contacts_delete'),

    path('contacts/create/', views.ContactCreateView,name='contacts_create'),



    path('contacts/update/<int:pk>/', views.ContactUpdateView,name='contacts_update'),
]

