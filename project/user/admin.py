from django.contrib import admin

# Register your models here.
# importing models from models.py to show at admin dashboard


from .models import *
admin.site.register(User)