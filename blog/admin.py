from django.contrib import admin
# ОБЯЗАТЕЛЬНО чтобы Blog вывелся в админку
from .models import Blog

admin.site.register(Blog)
# ОБЯЗАТЕЛЬНО