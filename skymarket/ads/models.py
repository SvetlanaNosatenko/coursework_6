from django.conf import settings
from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название товара",
                             help_text="Введите название товара")
    price = models.PositiveIntegerField(blank=True, null=True, verbose_name="Цена товара",
                                        help_text="Добавьте цену товара")
    description = models.CharField(max_length=1000, verbose_name="Описание товара",
                                   help_text="Введите описание товара")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=False)
    image = models.ImageField(upload_to="ad/", null=True, blank=True, verbose_name="Фото",
                              help_text="Разместите фото для объявления")

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ["created_at"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=500, verbose_name="Комментарий",
                            help_text="Оставьте свой комментарий здесь")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор комментария",
                               help_text="Выберите автора комментария")
    created_at = models.DateTimeField(auto_now_add=False, null=True, verbose_name="Время создания комментария",
                                      help_text="Введите время создания комментария")
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name="Объявление",
                           help_text="Добавьте объявление, которое относится к комментарию")
