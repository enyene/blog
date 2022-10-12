from django.contrib import admin
from .models import Category,Post,Comment
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields= {'slug':['name']}

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['title']}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment)