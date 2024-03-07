from django.db import models
from apps.users.models import User


class Blog(models.Model):
    title = models.CharField(
        max_length=250, verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to="blog_image", verbose_name="Картинка"
    )
    created_at = models.DateField(
        auto_now=True
    )
    is_active = models.BooleanField(
        default=True
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="user_blogs"
    )

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"

    def __str__(self):
        return self.title


