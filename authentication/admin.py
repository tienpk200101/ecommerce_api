from django.contrib import admin
from authentication.models import Person, Group, Membership

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'email']
    list_display = ['first_name', 'last_name', 'email', 'birth_date', "view_first_name"]
    list_filter = ['birth_date',]

    @admin.display(empty_value="???")
    def view_first_name(self, obj):
        return obj.first_name


class GroupAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']


class MembershipAdmin(admin.ModelAdmin):
    search_fields = ['user', 'group']
    list_display = ['user', 'group']


admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Membership)