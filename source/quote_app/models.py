from django.db import models

status_choices = [('new', 'новая'), ('moderated', 'модерированная')]


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


    # Create your models here.
    # текст - текстовое поле;
    # имя добавившего - строка;
    # email добавившего - поле для email-а;
    # рейтинг - целое число, по умолчанию 0;
    # статус - новая или модерированная, по умолчанию - новая;
    # дата и время добавления - автозаполнение.

class Quote(BaseModel):
    text = models.TextField(max_length=500, null=False, blank=False, verbose_name='Текст')
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Имя добавившего')
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='емаил')
    rating = models.IntegerField(null=True, blank=True, default=0,  verbose_name='рейтинг')
    status = models.CharField(max_length=50, null=False,
                              blank=False,
                              choices=status_choices,
                              default='new', verbose_name='статус')


