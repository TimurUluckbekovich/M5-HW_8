from django.db import models

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator

# Create your models here.
User = get_user_model()


class CategoryChoices(models.TextChoices):
    REPAIR = 'repair', 'Ремонт'
    CLEANING = 'cleaning', 'Уборка'
    EDUCATION = 'education', 'Обучение'
    BEAUTY = 'beauty', 'Красота'
    IT = 'it', 'IT'
    OTHER = 'other', 'Другое'


class Service(models.Model):
    title = models.CharField(
        max_length=255, 
        validators=[MinLengthValidator(5)],
        verbose_name="Название услуги"
    )
    description = models.TextField(verbose_name="Описание")
    category = models.CharField(
        max_length=50, 
        choices=CategoryChoices.choices, 
        default=CategoryChoices.OTHER,
        verbose_name="Категория"
    )
    base_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0)],
        verbose_name="Базовая цена"
    )
    discount = models.IntegerField(
        default=0, 
        validators=[MinValueValidator(0), MaxValueValidator(90)],
        verbose_name="Скидка (%)"
    )
    is_active = models.BooleanField(default=True, verbose_name="Принимаю заказы сейчас")
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='services',
        verbose_name="Мастер"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def final_price(self):
        price = float(self.base_price)
        discount_amount = price * (self.discount / 100)
        return round(price - discount_amount, 2)

    def __str__(self):
        return self.title


class Order(models.Model):
    service = models.ForeignKey(
        Service, 
        on_delete=models.CASCADE, 
        related_name='orders',
        verbose_name="Услуга"
    )
    client_name = models.CharField(max_length=100, verbose_name="Имя клиента")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    comment = models.TextField(blank=True, null=True, verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заявка от {self.client_name} на '{self.service.title}'"