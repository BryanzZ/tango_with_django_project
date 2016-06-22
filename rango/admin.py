from django.contrib import admin
from rango.models import Category, Page


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'views', 'likes']
    list_display = ('name', 'views', 'likes')

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'views', 'category')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
