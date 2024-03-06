from django.contrib import admin
from posts.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'photo')
    list_display_links = ('id', 'user')
    list_editable = ('title', 'photo')
    search_fields = (
        'user__username',
        'user__email',
        'title'
    )
    list_filter = (
        'created',
        'modified'
    )

    fieldsets = (
        ('Post', {
            'fields': (('user', 'title', 'photo'),)
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),)
        })
    )

    readonly_fields = ('created', 'modified')