from datetime import datetime

from django.db import models
from django.utils import timezone

# from django.utils.html import format_html
# from django.urls import reverse

# Create your models here.


class SavestUser(models.Model):
    first_name= models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    email= models.EmailField()
    creation_date= models.DateTimeField(default=timezone.now)
    active=models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    # def action_buttons(self):
    #   return format_html(
    #       '<a class="button" href="{}" >Active</a> &nbsp;'
    #       '<a class="button" href="{}">Inactive</a>',
    #   )
    # action_buttons.short_description = 'Action Buttons'
    # action_buttons.allow_tags = True
