from django.contrib import admin
from .models import *
class ProfAdmin(admin.ModelAdmin):
    list_display = ('pseudonym',)

class AccAdmin(admin.ModelAdmin):
    list_display = ('pseudonym', 'day_payment')
admin.site.register(Account, AccAdmin)
admin.site.register(Status)
admin.site.register(month)
admin.site.register(Profile, ProfAdmin)
admin.site.register(subscribersbot)
admin.site.register(typing)
admin.site.register(storage)
admin.site.register(security)
admin.site.register(changing)
admin.site.register(card)
admin.site.register(stories)
admin.site.register(acc_pre_value)
admin.site.register(prof_pre_value)
admin.site.register(sendmessage)
admin.site.register(contract)
admin.site.register(Audio)
admin.site.register(Video)
