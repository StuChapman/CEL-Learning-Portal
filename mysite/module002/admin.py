from django.contrib import admin

# Register your models here.

from .models import Pages, Tests, Answers

admin.site.register(Pages)
admin.site.register(Tests)
admin.site.register(Answers)