from django.contrib import admin
from .models import User, Item, Wish
# Register your models here.
class WishInline(admin.TabularInline):
    model = Wish
    list_display = ('user', 'item')

class UserAdmin(admin.ModelAdmin):
    inlines = [WishInline]
    list_display = ('f_name', 'l_name')
    search_fields = ('f_name', 'l_name')

class ItemAdmin(admin.ModelAdmin):
    inlines = [WishInline]
    list_display = ('name', 'create_by')
    search_fields = ('name', 'create_by')

admin.site.register(User, UserAdmin)
admin.site.register(Item, ItemAdmin)
