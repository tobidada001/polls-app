from django.contrib import admin
from .models import PollTitle, PollChoice
# Register your models here.
admin.site.register(PollTitle)
admin.site.register(PollChoice)
