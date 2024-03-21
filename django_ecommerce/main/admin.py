from django.contrib import admin
from .models import StatusReport, MarketingItem, Announcement, Badge

# Register your models here.
class StatusReportAdmin(admin.ModelAdmin):
    class Meta:
        model = StatusReport

class MarketingItemAdmin(admin.ModelAdmin):
    class Meta:
        model = MarketingItem

class AnnouncementAdmin(admin.ModelAdmin):
    class Meta:
        model = Announcement

class BadgeAdmin(admin.ModelAdmin):
    class Meta:
        model = Badge

admin.site.register(StatusReport, StatusReportAdmin)
admin.site.register(MarketingItem, MarketingItemAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Badge, BadgeAdmin)
