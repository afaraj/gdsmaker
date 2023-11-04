from django.contrib import admin
from .models import GDS

class GDSAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'frozen', 'created_at', 'updated_at')
    list_filter = ('frozen', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    ordering = ('created_at',)

admin.site.register(GDS, GDSAdmin)