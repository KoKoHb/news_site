from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "author", "updated_at", "get_image", "is_published")
    list_display_links = ("title",)
    list_editable = ("is_published",)
    exclude = ("author",)
    readonly_fields = ("get_image",)
    search_fields = ("title", "article")

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f"<img src={obj.image.url} width=100>")
        else:
            return "-"

    get_image.short_description = "Изображение"

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Category)
