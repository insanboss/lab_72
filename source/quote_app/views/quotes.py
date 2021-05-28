from rest_framework import viewsets
from quote_app.models import Quote
from quote_app.serializers.quote_serializer import QuoteSerializer


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
