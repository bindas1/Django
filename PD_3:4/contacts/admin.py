from django.contrib import admin
from django.utils.html import format_html

from django.utils.translation import gettext_lazy as _
from contacts.models import Person, Email, Address, Phone
from import_export.admin import ImportExportModelAdmin

admin.site.site_header = _('Addressbook')
admin.site.index_title = _('Dashboards')


class AddressInline(admin.StackedInline):
    model = Address
    extra = 0
    radio_fields = {
        'role': admin.HORIZONTAL
    }


class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 0


class EmailInline(admin.TabularInline):
    model = Email
    extra = 0


@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth', 'field_born_in_90', 'field_pesel']
    list_display_links = ['first_name', 'last_name']
    ordering = ['first_name', 'last_name']
    search_fields = ['^last_name']
    autocomplete_fields = ['friends']
    inlines = [AddressInline, PhoneInline, EmailInline]
    radio_fields = {
        'gender': admin.VERTICAL
    }
    fieldsets = [
        (None, {'fields': ['first_name', 'last_name']}),
        (_('Personal data'), {'fields': ['date_of_birth', 'pesel', 'image', 'gender', 'height']}),
        (_('Other'), {'fields': ['homepage', 'notes', 'friends']}),
    ]

    def field_born_in_90(self, model):
        if model.date_of_birth:
            return model.date_of_birth.strftime('%Y')[:3] == "199"

    field_born_in_90.boolean = True

    def field_pesel(self, model):
        if model.pesel:
            return format_html(f'<span style="color:red;">{model.pesel}</span>')
        return None

    field_pesel.empty_value_display = ""

    class Media:
        js = [
            'contacts/person.js'
        ]
        css = {'all': [
            'contacts/person.css'
        ]}
