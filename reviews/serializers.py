from django.contrib.auth.models import User

from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer

from reviews.models import Product, Category, Company, ProductSize, ProductSite, Comment, CustomerReportRecord

"""
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['pk', 'name', 'category']
        # pk and name to be serialized
        # exclude = ['category']    
        # editable=False set, and AutoField fields will be set to read-only by default
        # read_only_fields = ['name']
        # shortcut allowing you to specify arbitrary additional keyword arguments on fields
        # extra_kwargs = {'name': {'read_only': True}}
"""

class CompanySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Company
        fields = ['pk', 'name', 'url']


class CategorySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']
        expandable_fields = {
          'products': ('ProductSerializer', {'many': True})
        }



class ProductSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Product
        fields = ['pk', 'name', 'content', 'created', 'updated']
        expandable_fields = {
            'category': ('reviews.CategorySerializer', {'many': True}),
            'sites': ('reviews.ProductSiteSerializer', {'many': True}),
            'comments': ('reviews.CommentSerializer', {'many': True}),
        }


class ProductSiteSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductSite
        fields = ['pk', 'name', 'price', 'url', 'created', 'updated']
        expandable_fields = {
            'product': 'reviews.CategorySerializer',
            'productsize': 'reviews.ProductSizeSerializer',
            'company': 'reviews.CompanySerializer',
        }


class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CommentSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Comment
        fields = ['pk', 'title', 'content', 'created', 'updated']
        expandable_fields = {
            'product': 'reviews.CategorySerializer',
            'user': 'reviews.UserSerializer'
        }


# 
# With Django the validation is performed partially on the form, and partially on the model instance. 
# With Django Rest Framework the validation is performed entirely on the serializer class.
#
class CustomerReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerReportRecord

"""
#
# pecify custom field-level validation by adding validate_<field_name> methods to your Serializer subclass
#
def validate_title(self, value):
    if 'django' not in value.lower():
        raise serializers.ValidationError("error message")
    
    return value

#
# Object Level Validation - to do any other validation that requires access to multiple fields, add a method 
# called validate() to your Serializer subclass.
#
def validate(self, data):
    if data['start'] > data['finish']:
        raise serializers.ValidationError("finish must occur after start")
    return data

#
# Overriding Serializer Methods - if we want to be able to return complete object instances based on the validated 
# data we need to implement one or both of the create() and update() methods to our Serializer subclass.
#
def create(self, validated_data):
    return Comment.objects.create(**validated_data)


def update(self, instance, validated_data):
    instance.email = validated_data.get('email', instance.email)
    instance.title = validated_data.get('content', instance.title)
    instance.save()
    return instance

#
# Including extra context - you can provide arbitrary additional context by passing a context argument 
# when instantiating the serializer. The context dictionary can be used within any serializer field logic 
# by accessing the self.context attribute.
#
serializer = ProductSerializer(account, context={‘request’: request})

#
# Nested relationships - as opposed to previously discussed references to another entity, the referred entity 
# can instead also be embedded or nested in the representation of the object that refers to it. 
# Such nested relationships can be expressed by using serializers as fields. 
# If the field is used to represent a to-many relationship, you should add the many=True flag to the serializer field.
#

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']
        

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = ['pk', 'name', 'category']


#
# SerializerMethodField - this is a read-only field. It gets its value by calling a method on the serializer class it is attached to. 
# It can be used to add any sort of data to the serialized representation of your object.
#

#
# FlexFields (DRF-FF) for Django REST Framework is a package designed to provide a common baseline of functionality for dynamically 
# setting fields and nested models within DRF serializers. This package is designed for simplicity, with minimal magic and entanglement 
# with DRF's foundational classes. https://github.com/rsinger86/drf-flex-fields
# To define expandable fields, add an expandable_fields dictionary to your serializer’s Meta class.
#
# Expanding a Relationship
#
expandable_fields = {
 'category': CategorySerializer’
}
#
# Expanding a “Many” Relationship
#
expandable_fields = {
 'category': (CategorySerializer’, {‘many’: True})
}
#
# Open reviews/serializers.py and replace the current serializer classes
#

class CategorySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']


class ProductSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Product
        fields = ['pk', 'name', 'content', 'created', 'updated']
        expandable_fields = {
          'category': (CategorySerializer, {'many': True})
        }

# http://127.0.0.1:8000/product/?fields=pk,name   
# http://127.0.0.1:8000/product/?omit=content
# http://127.0.0.1:8000/product/?expand=category
# http://127.0.0.1:8000/product/?expand=category&fields=name,category.name

#
# To avoid circular import problems, it’s possible to lazily evaluate a string reference to you serializer class using this syntax:
#
expandable_fields = {
  'category': ('reviews.CategorySerializer', {'many': True})
}
"""