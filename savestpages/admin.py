from django.contrib import admin

from django.http import HttpResponseRedirect
from django.conf.urls import url
# from django.urls import path

from django.utils.html import format_html
from django.urls import reverse

from django.contrib.auth.models import User, Group
from .models import SavestUser


# Register your models here.
admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.site_header = "Savest Admin"
admin.site.site_title = "Savest Admin Portal"
admin.site.index_title = "Welcome to the Savest Admin Portal"


@admin.register(SavestUser)
class SavestUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'email',
                    'creation_date', 'action_buttons', 'active')
    list_filter = ('creation_date',)
    ordering = ('last_name',)
    search_fields = ('last_name',)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url(r'^(?P<savestuser_id>.+)/active/$',
                self.admin_site.admin_view(self.process_active), name='user-active'),

            url(r'^(?P<savestuser_id>.+)/inactive/$',
                self.admin_site.admin_view(self.process_inactive), name='user-inactive'),
        ]
        return custom_urls + urls

    def action_buttons(self, obj):
        return format_html(
            '<a class="button" href="{}" >Set Active</a> &nbsp;'
            '<a class="button" href="{}">Set Inactive</a>',
            reverse('admin:user-active', args=[obj.pk]),
            reverse('admin:user-inactive', args=[obj.pk]),
        )
    action_buttons.short_description = 'Action Buttons'
    action_buttons.allow_tags = True

    def process_active(self, request):
      self.object.all().update(active=True)
      self.message_user(request, "User set to active")
      return HttpResponseRedirect(url)

    def process_inactive(self, request):
      self.object.all().update(active=True)
      self.message_user(request, "Successfully set to inactive")
      return HttpResponseRedirect(url)

    def process_action(self, request, savestuser_id):
      return('Yes')
