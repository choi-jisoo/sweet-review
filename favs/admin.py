from django.contrib import admin
from . import models


@admin.register(models.FavList)
class FavListAdmin(admin.ModelAdmin):

    """Custom Favourite List Admin"""

    list_display = ("created_by",)
