from django.contrib import admin
from .models import SignUpData,packages,custom,destination
# Register your models here.
admin.site.register(SignUpData)
admin.site.register(packages)
admin.site.register(custom)
admin.site.register(destination)