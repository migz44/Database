from django.contrib import admin

from database_app.models import Customer

admin.site.site_title = ('MASSIVE INC ENTERPRICES')
admin.site.site_header = ('MASSIVE ENTERPRICES')

# HOW TO CUSTOMISE DJANGO ADMIN
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display =['names', 'email', 'gender']
    list_per_page = 20
    search_fields = ['names', 'email','dob','phone']
    list_filter = ['gender']
admin.site.register(Customer, CustomerAdmin)






