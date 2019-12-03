from django.contrib import admin

from contacts.models import Persons

@admin.register(Persons)
class PersonsAdmin(admin.ModelAdmin):
    pass
