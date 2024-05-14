from django.contrib import admin
from . models import Link, Category

admin.site.register(Link)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug' : ('category_name', )}
	list_filter = ["category_name"]