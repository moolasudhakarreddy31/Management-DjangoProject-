from django.contrib import admin

from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_filter = ('status', 'assignee')
    list_display = ('id', 'title', 'status', 'assignee', 'description', 'updated_at')
    search_fields = ['title','status']

admin.site.site_header = "Appollo Ticket Admin"
admin.site.site_title = 'Appollo Ticket Administration'
admin.site.index_title = 'Appollo Ticket Administration'
admin.site.register(Ticket, TicketAdmin)