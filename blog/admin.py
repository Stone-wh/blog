from django.contrib import admin

# Register your models here.
from .models import Post,Category,Tag

class PostAdmin(admin.ModelAdmin):
	list_display = ['title','created_time','modified_time','category','author',]
	fields = ['title','body','excerpt','category','tags','author',]

	def save_mode(self,request,obj,form,change):
		obj.author = request.author
		super().save_mode(request,obj,form,change)

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)

