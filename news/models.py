from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    article = models.TextField("Статья")
    created_at = models.DateTimeField("Время создания", auto_now_add=True)
    updated_at = models.DateTimeField("Последнее обновление", auto_now=True)
    is_published = models.BooleanField("Опубликовано?", default=False)
    image = models.ImageField("Картинка к посту", upload_to='posts/%Y/%m/%d/', blank=True, null=True)
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", verbose_name="Категория", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-updated_at"]


class Category(models.Model):
    name = models.CharField("Категория", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"
        ordering = ["name"]
