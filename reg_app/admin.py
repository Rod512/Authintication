from django.contrib import admin
from reg_app.models import user

@admin.register(user)
class userAdmin(admin.ModelAdmin):
    list_display =('name','email','password','retype_pass')
    


