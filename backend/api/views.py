import json
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer

@api_view(['GET', 'POST'])
def api_home(request, *args, **kwargs):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data)

    elif request.method == 'GET':
        instance = Product.objects.all().order_by('?').first()
        data = {}

        if instance:
            data = ProductSerializer(instance).data

        return Response(data)