from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.views import View

from quote_app.models import Quote


class IncreaseRating(View):

    def get(self, request, *args, **kwargs):
        quote = get_object_or_404(Quote, pk=self.kwargs.get('pk'))
        user = request.user
        quote.rating +=1
        quote.save()


class DecreaseRating(View):
    def get(self, request, *args, **kwargs):
        quote = get_object_or_404(Quote, pk=self.kwargs.get('pk'))
        user = request.user
        quote.rating -= 1
        quote.save()
