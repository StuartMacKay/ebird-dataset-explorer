from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from django.utils.translation import gettext_lazy as _

from .models import Update


@register(Update)
class UpdateAdmin(ModelAdmin):
    list_display = ("display_title", "published_at")
    search_fields = ("title",)
    ordering = ("-published_at",)

    @admin.display(description=_("Title"))
    def display_title(self, instance):
        return instance.get_title()
