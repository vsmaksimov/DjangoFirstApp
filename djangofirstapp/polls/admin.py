from django.contrib import admin
from .models import CustomUser
from .models import Question
from .models import Choice

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Question)
admin.site.register(Choice)

