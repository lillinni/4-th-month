from django.db import models
from main_page.models import Book

class Order(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя заказчика")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    email = models.EmailField(null=True, blank=True, verbose_name="Email")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Выбранная книга")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ для {self.name} на книгу {self.book.title}"
