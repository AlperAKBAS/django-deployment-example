from django.contrib import admin
from .models import UserProfileInfo
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.


class UserProfileInfoAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html(
            f'<img src="{object.profile_pic.url}" width="60" style="border-radius: 10px"/>'
        )

    def user_name(self, object):
        return object.user.username

    def user_email(self, object):
        return object.user.email

    thumbnail.short_description = 'Profile Pic'

    list_display = ['id', 'thumbnail', 'user_name', 'user_email']
    list_display_links = ['id', 'thumbnail', ]


admin.site.register(UserProfileInfo, UserProfileInfoAdmin)


#https://stackoverflow.com/questions/2270537/how-to-customize-the-auth-user-admin-page-in-django-crud
# class CustomUserAdmin(UserAdmin):
#     def __init__(self, *args, **kwargs):
#         super(UserAdmin,self).__init__(*args, **kwargs)
#         UserAdmin.list_display = list(UserAdmin.list_display) + ['date_joined']
#         UserAdmin.list_display.insert(0,'thumbnail')

#     # Function to count objects of each user from another Model (where user is FK)
#     def thumbnail(self, object):
#         return format_html(
#             f'<img src="{UserProfileInfo.objects.get(pk=object.id).profile_pic.url}" width="60" style="border-radius: 10px"/>'
#         )


# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)