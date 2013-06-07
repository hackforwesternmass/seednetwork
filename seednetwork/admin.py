from django.contrib import admin

from seednetwork.models import MemberInfo

class MemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email',
                    'town', 'phone', 'street_address', 'include_in_member_profiles')
    search_fields = ['town', 'phone', 'street_address', 'include_in_member_profiles']
    list_filter = ['town', 'include_in_member_profiles']

    def email(self, instance):
       return instance.user.email
    def name(self, instance):
       return instance.user.first_name + ' ' + instance.user.last_name
    
    
admin.site.register(MemberInfo, MemberAdmin)
