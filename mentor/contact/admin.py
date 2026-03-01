from django.contrib import admin
from contact.models import Contactform

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')

admin.site.register(Contactform, ContactAdmin)

# Register your models here.
