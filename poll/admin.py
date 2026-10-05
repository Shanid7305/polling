from django.contrib import admin
from poll.models import CustomUser,Poll,Choices
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Poll)
admin.site.register(Choices)