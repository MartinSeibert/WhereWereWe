from django.contrib import admin
from main.models import  Show, UserProfile



# Add this class to customize the admin interface
class ShowAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}

# Register your models here.

admin.site.register(Show, ShowAdmin)
admin.site.register(UserProfile)