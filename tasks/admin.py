from django.contrib import admin

from .models import *

admin.site.site_header = "To Do App"
admin.site.site_title = "To Do App"
admin.site.index_title = "To Do"

admin.site.register(Task)
