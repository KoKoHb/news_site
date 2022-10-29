from .models import Category


class CategoryMixin:
    def get_category(self, **kwargs):
        context = kwargs
        context["cats"] = Category.objects.filter(post__isnull=False)
        return context

