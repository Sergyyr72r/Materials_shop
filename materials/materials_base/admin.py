from django.contrib import admin
from .models import Material


class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'photo',
        )
    list_editable = ('description',)
    search_fields = ('name', 'distributor')
    list_filter = ('name',)
    empty_value_display = '-пусто-'


admin.site.register(Material, MaterialAdmin)
