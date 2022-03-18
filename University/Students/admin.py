from django.contrib import admin

from .models import Students, Groups


class StudentsAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name','patronymic','date_of_birth', 'series','number', 'group_name')
    list_display_links = ('last_name',)
    search_fields = ('last_name',)


class GroupsAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_students')
    list_display_links = ('name',)




admin.site.register(Students, StudentsAdmin)
admin.site.register(Groups, GroupsAdmin)
admin.site.site_title = 'Университет'
admin.site.site_header = 'Университет'
