from django.contrib import admin

from .models.chart import MonthByMonth, MonthView, Channel

admin.site.register(MonthByMonth)
admin.site.register(MonthView)
admin.site.register(Channel)
