from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("display_title", "level", "published", "expired")
    list_filter = ("level",)
    search_fields = ("title",)
    ordering = ("-published",)

    @admin.display(description=_("Title"))
    def display_title(self, instance):
        return instance.get_title()
