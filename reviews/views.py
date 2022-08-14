from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from reviews.serializers import ProductSerializer
from reviews.models import Product

#
# Django Rest-Framework supports two different types of views.
#
# 1 — Function Based Views
# 2 — Class Based Views (Generic Views, ViewSets)
#
# We’ll use ViewSets (Class Based Views).
# ViewSets works exactly same as Generic Views. The only difference is using ViewSet you don’t have to create separate 
# views for getting list of objects and detail of one object. We do not configure the urls with ViewSets. 
# Routers generates urls for ViewSets automatically and binds methods for different request method types.
#
# GenericViewSet
# The GenericViewSet class does not provide any actions/methods by default such as GET, POST, PUT but does include 
# the base set of generic view behavior, such as the get_object and get_queryset methods.
#
# ReadOnlyModelViewSet
# A viewset that provides default list() and retrieve() actions. It accepts only the request method type GET.
#
# ModelViewSet
# A viewset that provides default create(), retrieve(), update(), partial_update(), destroy() and list() actions.
#
# |--------------|---------|------------------|----------------------|
# | ENDPOINT     | METHOD  | ACTION           | DESCRIPTION          |
# |--------------|---------|------------------|----------------------|
# | products/    | GET     | list()           | Get all products     |
# | products/    | POST    | create()         | Create new product   |
# | products/:pk | GET     | retrieve()       | Get product details  | 
# | products/:pk | PUT     | update()         | Update product       |
# | products/:pk | PATCH   | partial_update() | Part. update product |
# | products/:pk | DELETE  | delete()         | Delete product       |
# |--------------|---------|------------------|----------------------|

class ProductViewSet(ReadOnlyModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()

#
# You’ll need yo set queryset and serializer_class attributes or override get_queryset() and get_serializer_class() methods.
# ProductViewSet extended from ReadOnlyModelViewSet. Our viewset provides only get actions.
#
# |--------------|---------|------------------|----------------------|
# | ENDPOINT     | METHOD  | ACTION           | DESCRIPTION          |
# |--------------|---------|------------------|----------------------|
# | products/    | GET     | list()           | Get all products     |
# | products/:pk | GET     | retrieve()       | Get product details  |
# |--------------|---------|------------------|----------------------|

#
# Marking extra actions for routing
#
# If you have ad-hoc methods that should be routable, you can mark them as such with the @action decorator. 
# Like regular actions, extra actions may be intended for either a single object, or an entire collection. 
# To indicate this, set the detail argument to True or False. The router will configure its URL patterns accordingly.
#
"""
class ProductViewSet(ReadOnlyModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
    @action(detail=False)
    def get_list(self, request):
        pass
      
    @action(detail=True)
    def get_product(self, request, pk=None):
        pass


    @action(detail=True, methods=['post', 'delete'])
    def delete_product(self, request, pk=None):
        pass
"""

# |-----------------------------|---------|----------------------|
# | ENDPOINT                    | METHOD  | ACTION               |
# |-----------------------------|---------|----------------------|
# | products/                   | GET     | list()               |
# | products/:pk                | GET     | retrieve()           |
# | products/get_list           | GET     | get_list()           |
# | products/get_product/:pk    | GET     | get_product()        |
# | products/delete_product/:pk | DELETE  | delete_product()     |
# | products/delete_product/:pk | POST    | delete_product()     |
# |-----------------------------|---------|----------------------|