from rest_framework import serializers
from quote_app.models import Quote


class QuoteSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('text', 'name', 'email', 'rating', 'status')
