from django.contrib import admin
from .models import Register, Bank, Journal

# Register your models here.
admin.site.register(Register)
admin.site.register(Bank)

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
     list_display = ("TransactionId", "Receiver", "Amount", "TimeDate")
