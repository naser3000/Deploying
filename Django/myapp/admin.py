from django.contrib import admin
from .models import Weblog, Post, Comment, User

admin.site.site_header = 'Illumination'
admin.site.site_title = 'Illumination'
admin.site.index_title = 'Illumination administration'
class UserAdmin(admin.ModelAdmin):
	#date_hierarchy = 'created'
	list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'password')
	list_filter = ('id', 'username', 'first_name', 'last_name', 'email')
	search_fields = ('id', 'username', 'first_name', 'last_name', 'email')
	#prepopulated_fields = {'username': ('name'),}


class WeblogAdmin(admin.ModelAdmin):
	list_display = ('id', 'weblog_auther', 'weblog_date')
	list_filter = ('id', 'weblog_auther', 'weblog_date')
	search_fields = ('id', 'weblog_auther', 'weblog_date')



class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'post_title', 'post_date', 'weblog')
	list_filter = ('id', 'post_title', 'post_date', 'weblog')
	search_fields = ('id', 'post_title', 'post_date', 'weblog')
#	fieldsets = (
#        (None, {
#            'fields': ('post_title', 'post_summary', 'post_text', 'post_date')
#        }),
#        ('Advanced options', {
#            'classes': ('collapse',),
#            'fields': (),
#        }),
#    )



class CommentAdmin(admin.ModelAdmin):
	list_display = ('id', 'comment_auther', 'comment_date')
	list_filter = ('id', 'comment_auther', 'post', 'comment_date')
	search_fields = ('id', 'comment_auther', 'post', 'comment_date')



admin.site.register(Weblog, WeblogAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(User, UserAdmin)



