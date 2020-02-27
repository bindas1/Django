from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from contacts.models import Person, Email, Address, Phone

admin.site.site_header = _("Address book")
admin.site.index_title = _("Dashboards")


class EmailInline(admin.TabularInline):
    model = Email
    extra = 0


class AddressInline(admin.StackedInline):
    model = Address
    extra = 0


class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 0


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [EmailInline, AddressInline, PhoneInline]
    radio_fields = {
        'gender': admin.VERTICAL
    }
