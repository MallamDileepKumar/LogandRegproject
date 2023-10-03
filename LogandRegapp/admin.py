from django.contrib import admin
from .models import Register
# Register your models here.
class RegAdmin(admin.ModelAdmin):
    list_display=('Fname','Lname','FLname','Address','Email','password','re_password','Mobile')
admin.site.register(Register,RegAdmin)
