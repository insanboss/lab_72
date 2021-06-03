from rest_framework import serializers
from quote_app.models import Quote

# class Quote(BaseModel):
#     text = models.TextField(max_length=500, null=False, blank=False, verbose_name='Текст')
#     name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Имя добавившего')
#     email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='емаил')
#     rating = models.IntegerField(null=True, blank=True, default=0,  verbose_name='рейтинг')
#     status = models.CharField(max_length=50, null=False,
#                               blank=False,
#                               choices=status_choices,
#                               default='new', verbose_name='статус')


class QuoteSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('id', 'text', 'name', 'email', 'rating', 'status', 'created_at')
