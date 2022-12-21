from django.contrib import admin
from .models import NewsStory
admin.site.register(NewsStory)
# Register your models here.

from .models import Category

admin.site.register(Category)