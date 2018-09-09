from django.contrib import admin
from api.models import Person, Account, Log


admin.site.register(Person)
admin.site.register(Account)


@admin.register(Log)
class Log(admin.ModelAdmin):
    readonly_fields = ('date',)