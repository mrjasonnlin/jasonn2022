from django.contrib import admin
from article.models import Article, Comment
from upload_profile.models import Photo


class CommentAdmin(admin.ModelAdmin):
    list_display = ['article', 'content', 'pubDateTime']
    list_display_links = ['article']
    list_filter = ['article', 'content']
    search_fields = ['content']
    list_editable = ['content']

    class Meta:
        model = Comment


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'user_image', 'upload_date', 'introduce']

    def user_image(self, obj):
        return '<img src="/static/%s" hight="64" width="64" / ' % obj.photo
    user_image.allow_tags = True
    user_image.short_description = "圖片"

    list_display_links = ['user_name']
    list_filter = ['user_name', 'upload_date']
    search_fields = ['upload_date']
    list_editable = ['upload_date']

    class Meta:
        model = Photo


admin.site.register(Article)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Comment, CommentAdmin)
