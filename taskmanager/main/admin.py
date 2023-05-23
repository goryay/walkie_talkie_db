from django.contrib import admin
from .models import Contact, Task
#from .models import Profile

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Task)

# Register your models here.
# admin.site.register(Profile)