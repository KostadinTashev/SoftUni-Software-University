# 'department's app urls.py
from django.urls import path

from departments_app.departments.views import show_departments, show_department_details, redirect_to_fist_department, \
    show_not_found

urlpatterns = (
    # /departments/
    path('', show_departments, name='show departments'),

    path('not-found/', show_not_found, name='not found'),
    # /departments/{department_id}/
    path('<department_id>/', show_department_details, name='redirect demo'),
    # /departments/int/{department_id}
    path('int/<int:department_id>/', show_department_details, name='show department details with string'),
    path('redirect/', redirect_to_fist_department, name='show departments details'),
)
