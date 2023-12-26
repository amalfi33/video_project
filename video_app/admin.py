from django.contrib import admin
from .models import Post , Image
# Register your models here.
class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, SlugAdmin)
admin.site.register(Image)
