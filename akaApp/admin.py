from django.contrib import admin
from akaApp.models import *
from mptt.admin import MPTTModelAdmin

class dateOrder(admin.ModelAdmin):
	readonly_fields = ('date',)

admin.site.register(Article, dateOrder)
admin.site.register(Comment, MPTTModelAdmin)
