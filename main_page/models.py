from django.db import models

class Book(models.Model):
    GENRE_CHOICES = (
        ('Фантастика', 'Фантастика'),
        ('Романтика', 'Романтика'),
        ('Приключения', 'Приключения'),
    )
    
    title = models.CharField(
        max_length=200,
        verbose_name='Укажите название книги'  
    )  
    description = models.TextField(
        verbose_name='Описание книги'  
    )  
    cover_image = models.ImageField(
        upload_to='book_covers/',
        blank=True, null=True,
        verbose_name='Обложка книги'  
    )  
    price = models.DecimalField(
        max_digits=10, decimal_places=2,
        verbose_name='Цена книги'  
    )  
    release_date = models.DateField(
        verbose_name='Дата выхода книги'  
    )  
    genre = models.CharField(
        max_length=100,
        choices=GENRE_CHOICES,  
        verbose_name='Жанр книги'  
    )  
    author_email = models.EmailField(
        verbose_name='Почта автора'  
    )  
    author_name = models.CharField(
        max_length=100,
        verbose_name='Имя автора'  
    )  
    youtube_link = models.URLField(
        blank=True, null=True,
        verbose_name='Ссылка на YouTube'  
    )
    created_at = models.DateTimeField(
        auto_now_add=True,  
        verbose_name='Дата и время создания'  
    )


    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.title}-{self.price}'