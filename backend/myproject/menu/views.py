from rest_framework import viewsets
from .models import Dish
from .serializers import DishSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

    @action(detail=True, methods=['post'])
    def toggle_publish(self, request, pk=None):
        dish = self.get_object()
        dish.isPublished = not dish.isPublished
        dish.save()
        return Response({'status': 'publish status updated', 'isPublished': dish.isPublished})
