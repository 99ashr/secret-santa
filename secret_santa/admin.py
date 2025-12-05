from django.contrib import admin
from .models import Participant, DrawMapping


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')


@admin.register(DrawMapping)
class DrawMappingAdmin(admin.ModelAdmin):
    list_display = ('token', 'giver', 'recipient', 'is_revealed', 'created_at')
    list_filter = ('is_revealed', 'created_at')
    search_fields = ('token', 'giver__name', 'recipient__name')
    readonly_fields = ('token', 'created_at', 'revealed_at')
    
    fieldsets = (
        ('Token & Mapping', {
            'fields': ('token', 'giver', 'recipient')
        }),
        ('Status', {
            'fields': ('is_revealed', 'created_at', 'revealed_at')
        }),
    )
