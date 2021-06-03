from rest_framework import viewsets
from quote_app.models import Quote
from quote_app.permissions import QuotePermission
from quote_app.serializers.quote_serializer_get import QuoteSerializerGet
from quote_app.serializers.quote_serializer_post import QuoteSerializerPost


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializerGet
    permission_classes = [QuotePermission]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return QuoteSerializerPost
        elif self.request.method == "GET":
            return QuoteSerializerGet

    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset)
        if self.request.user.is_authenticated and self.request.user.has_perm('quote_app.list_quotes'):
            return queryset
        else:
            return queryset.filter(status='moderated')
