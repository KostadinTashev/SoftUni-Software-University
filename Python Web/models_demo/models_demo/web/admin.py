from django.contrib import admin

from models_demo.web.models import Employee, NullBlankDemo, Department, Project, Category


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("name",)}


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'level', 'department')
    list_filter = ('level', 'department', 'first_name')
    search_fields = ('first_name', 'last_name')
    sortable_by = ('first_name', 'last_name')

    # fields = [('first_name', 'last_name'), 'level']

    fieldsets = (
        (
            'Personal Info',
            {
                'fields': ('first_name', 'last_name', 'age', 'email'),
            }
        ),
        (
            'Professional Info',
            {
                'fields': ('level', 'years_of_experience'),
            }
        ),
        (
            'Company Info',
            {
                'fields': ('department', 'is_full_time', 'start_date')
            }
        )
    )

    # def has_delete_permission(self, request, obj=None):
    #     return False


@admin.register(NullBlankDemo)
class NullBlankDemoAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
