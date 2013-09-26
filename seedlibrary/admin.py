from django.contrib import admin
from seedlibrary.models import Seed, Event

class SeedAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 
                    'seed_type', 'crop_type', 'seed_variety', 'enough_to_share')
    search_fields = ['seed_type', 'crop_type', 'seed_variety']
    list_filter = ['seed_type','crop_type', 'enough_to_share']
   
    def name(self, instance):
       return instance.user.first_name + ' ' + instance.user.last_name
    def email(self, instance):
       return instance.user.email
    
admin.site.register(Seed,SeedAdmin)
admin.site.register(Event)
