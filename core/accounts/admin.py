from django.contrib import admin

# Register your models here.
from accounts.models import User

class UserAdmin(admin.ModelAdmin):
    fields = [
        "username",
        "first_name",
        "last_name",
        "email",
        "password",
        "is_staff",
        "is_active",
        "date_joined",
    ]

admin.site.register(User, UserAdmin)
