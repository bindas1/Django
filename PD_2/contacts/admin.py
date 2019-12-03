from django.contrib import admin

from contacts.models import Person, EmailField, PhoneNumber, Address


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(EmailField)
class EmailFieldAdmin(admin.ModelAdmin):
    pass


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass
