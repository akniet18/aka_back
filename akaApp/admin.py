from django.contrib import admin
from akaApp.models import *

class dateOrder(admin.ModelAdmin):
	readonly_fields = ('date',)

admin.site.register(Article, dateOrder)
admin.site.register(Comment, dateOrder)
