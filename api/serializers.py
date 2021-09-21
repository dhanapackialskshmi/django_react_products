#from django.db.models import field
from django.db.models import fields
from rest_framework import serializers
from .models import *
from collections import namedtuple



class DimensionsSerializers(serializers.ModelSerializer):
    base_id=serializers.IntegerField(required=False)
    product_id=serializers.IntegerField(required=False)
 
 
    class Meta:
        model = Dimensions
        #fields = ['length','width','height','base_id','product_id']
        fields='__all__'

class ImagesSerializers(serializers.ModelSerializer):
    base_id=serializers.IntegerField(required=False)
    product_id=serializers.IntegerField(required=False)
 
    class Meta:
        model = Images
        #fields = ['name','is_listimage','url','base_id','product_id']
        fields='__all__'
        

class PropertiesSerializers(serializers.ModelSerializer):
    base_id=serializers.IntegerField(required=False)
    product_id=serializers.IntegerField(required=False)
    
    dimension=DimensionsSerializers(read_only=True,many=False)
    image  = ImagesSerializers(read_only=True,many=True)
  
    
    class Meta:
        model = Properties
        #fields= ['base_id','product_id','original_price','price','dimension','image']
        fields='__all__'

        
         

class BasetableSerializers(serializers.ModelSerializer):

    properties=PropertiesSerializers(read_only=True,many=True)
    print(properties)
    #dimensions=DimensionsSerializers(read_only=True,many=True)
    #images=ImagesSerializers(read_only=True,many=True)
    
    #Timeline = namedtuple('Basetable', ('properties','dimensions','images'))
    class Meta:
        model=Basetable
        fields= ['productname','description','properties']

    
    
    print("yessssss")

        


