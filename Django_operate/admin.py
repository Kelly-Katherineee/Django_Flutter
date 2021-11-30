from django.contrib import admin

# Register your models here.
from Django_operate.models import Users, UserInfo

admin.site.register(Users)
admin.site.register(UserInfo)
