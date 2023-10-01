from django.contrib import admin
from posts.models import Product, Category


# Register your models here.
@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'created_date', 'modified_date')
    list_filter = ('price',)
    search_fields = ('name', 'description',)
    list_editable = ('name',)


admin.site.register(Category)
