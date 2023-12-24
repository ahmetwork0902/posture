from django.contrib import admin
from .models import Users, Sessions, Wrong_pose, Users_achievements, Achievements

# Register your models here.
@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'time_create']
    list_editable = ['email']
    ordering=['-time_create']


admin.site.register(Sessions)
admin.site.register(Wrong_pose)
admin.site.register(Users_achievements)
admin.site.register(Achievements)
