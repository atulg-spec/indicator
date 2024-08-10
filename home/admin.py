from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from social_django.models import Nonce,UserSocialAuth,Association
from social_django.admin import Nonce,UserSocialAuth,Association

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email','phone_number' ,'first_name', 'is_suscribed', 'is_active', 'is_staff')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email','phone_number' ,'first_name', 'last_name')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email','phone_number', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Suscription Details', {'fields': ('is_suscribed',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        return formfield

# Register the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Contact)
class contact_us(admin.ModelAdmin):
    list_display = ('user','name','phone_number','query','date_time')
    list_filter = ('user','date_time',)
    search_fields = ('user','name','email','query')


admin.site.unregister(Nonce)
admin.site.unregister(UserSocialAuth)
admin.site.unregister(Association)


# ----------Admin Customization------------
admin.site.site_header = "Start Market Admin"
admin.site.site_title = "Start Market Indicators Management"
admin.site.index_title = "Admin"
admin.site.unregister(Group)