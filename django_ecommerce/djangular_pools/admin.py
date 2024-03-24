from django.contrib import admin
from .models import Poll, PollItem

# Register your models here.
class PollItemAdmin(admin.ModelAdmin):
    class Meta:
        model = PollItem

class PollAdmin(admin.ModelAdmin):
    class Meta:
        model = Poll

admin.site.register(Poll, PollAdmin)
admin.site.register(PollItem, PollItemAdmin)