from django.contrib import admin
from main.models import User, Show, Episode



# Add this class to customize the admin interface
class ShowAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}

class EpisodeAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}

# Register your models here.
admin.site.register(User)
admin.site.register(Show, ShowAdmin)
admin.site.register(Episode, EpisodeAdmin)