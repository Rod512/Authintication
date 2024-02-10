from django.contrib import admin
from reg_app.models import User

@admin.register(User)
class userAdmin(admin.ModelAdmin):
    list_display =('name','email','password','retype_pass')
    


