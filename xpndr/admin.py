from django.contrib import admin

# Register your models here.
from .models import Satellite, Transponder, Comment

admin.site.register(Satellite)
admin.site.register(Transponder)
# admin.site.register(Comment)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'satellite', 'transponder',
                    'complaint_type', 'issue_time')
    list_filter = ('user',   'complaint_type',
                   'issue_time', 'active', 'created', 'publish', 'satellite')
    search_fields = ('user_detail', 'impact')
    ordering = ('issue_time', 'date')
