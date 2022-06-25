from django.contrib import admin

# Register your models here.
from accounts.models import Users

admin.site.register(Users)