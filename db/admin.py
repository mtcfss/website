from django.contrib import admin
from .models import Member, Inscription, Event, EventLink

class InscriptionInline(admin.TabularInline):
    model = Inscription
    extra = 1

class EventLinkInline(admin.TabularInline):
    model = EventLink
    extra = 2

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'phone', 'email')
    inlines = [InscriptionInline]
    search_fields = ['name', 'family_name', 'inscription__course']
    list_filter = ['inscription__course', 'inscription',
                   'inscription__confirmed', 'inscription__dreamspark_key',
                   'inscription__member_card']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [EventLinkInline]

admin.site.register(Inscription)  # TODO: use class instead
admin.site.register(EventLink)  # TODO: use class instead
