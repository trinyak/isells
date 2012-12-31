from shop.models import Website, Plan
from django.contrib import admin

class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain', 'plan', 'created')

admin.site.register(Website, WebsiteAdmin)

class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price')

admin.site.register(Plan, PlanAdmin)

