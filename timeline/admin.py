from timeline.models import UserProfile, UserTeam
from django.contrib import admin
from timeline.models import UserProfile, TimeLineMessage
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(TimeLineMessage)
admin.site.register(UserTeam)
