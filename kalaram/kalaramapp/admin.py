from django.contrib import admin
from .models import Feedback, Donation

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    ordering = ('-created_at',)

admin.site.register(Feedback, FeedbackAdmin)



admin.site.register(Donation)