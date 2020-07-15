from django.contrib import admin
from .models import Category,Product
from django.utils.html import format_html 

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['thumbnail','image','name','price','stock','available','created','updated']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
    def thumbnail(self, obj):
        return format_html('<img src="{}" style="width: 80px; height: 80px;"/>'.format(obj.image.url))
    thumbnail.description = 'thumbnail'

admin.site.register(Product,ProductAdmin)