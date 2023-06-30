from django.contrib import admin

#SUPERUSER USERNAME/PW: admin/admin
#test username/pw: test/123test132
# Register your models here.

from django.contrib.auth.models import User
from .models import Vehicle,CustomUser,WishlistItem,Post

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username']

class PostAdmin(admin.ModelAdmin):
    list_display=['pk','user','vehicle']

class VehicleAdmin(admin.ModelAdmin):
    list_display=['make','model']



class WishListItemAdmin(admin.ModelAdmin):
    list_display = ['user','post']

admin.site.register(Post,PostAdmin)
admin.site.register(Vehicle,VehicleAdmin)
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(WishlistItem,WishListItemAdmin)