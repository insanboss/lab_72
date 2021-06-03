from django.urls import include, path
from rest_framework import routers
from quote_app import views
from quote_app.views.index import index

router = routers.DefaultRouter()
router.register(r'quotes', views.QuoteViewSet)

app_name = 'quote_app'

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('index/', index, name='index'),
]
