from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom.fields',
            {
                'fields':(
                    'fio',
                    'gender',
                    'birth_date',
                    'groups',
                )
            }
        )
    )
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom.fields',
            {
                'fields':(
                    'fio',
                    'gender',
                    'birth_date',
                )
            }
        )
    )


admin.site.register(CustomUser, CustomUserAdmin)