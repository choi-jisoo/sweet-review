from django.contrib import admin
from . import models


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):

    """Custon Person Admin"""

    list_display = (
        "name",
        "kind",
    )

    list_filter = ("kind",)
