from django.contrib import admin
from .models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

class PhotoInline(admin.TabularInline):
    model = Photo

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','slug','coment','createData','category','hits','available_post']
    prepopulated_fields = {'slug':('title',)}
    inlines = [PhotoInline]
