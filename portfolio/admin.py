# admin.py
from django.contrib import admin
from .models import ContactMessage


def get_all_field_names(model):
    return [field.name for field in model._meta.get_fields()]

class ContactMessageAdmin(admin.ModelAdmin):
    list_display=get_all_field_names(ContactMessage)

admin.site.register(ContactMessage,ContactMessageAdmin)


