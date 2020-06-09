from django.contrib import admin
from .models import List, ListItem


# Register your models here.
class ListAdmin(admin.ModelAdmin):
    pass


class ListItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(List, ListAdmin)
admin.site.register(ListItem, ListItemAdmin)
